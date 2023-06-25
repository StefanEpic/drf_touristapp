from .models import Mountain, MountainImage, Coord, User, Level
from rest_framework import serializers


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'second_name', 'last_name', 'email', 'phone']


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ['winter', 'summer', 'autumn', 'spring']


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coord
        fields = ['latitude', 'longitude', 'height']


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MountainImage
        fields = ['data', 'title']


class MountainSerializer(serializers.ModelSerializer):
    user = UsersSerializer()
    coords = CoordsSerializer()
    level = LevelSerializer()
    images = ImageSerializer(many=True)

    class Meta:
        model = Mountain
        fields = ['beauty_title', 'title', 'other_title', 'connect', 'add_time', 'user', 'coords', 'level', 'images',
                  'status']
        read_only_fields = ['pk', 'status', 'add_time']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        cords_data = validated_data.pop('coords')
        level_data = validated_data.pop('level')
        images_data = validated_data.pop('images')

        user = User.objects.create(**user_data)
        coords = Coord.objects.create(**cords_data)
        level = Level.objects.create(**level_data)

        instance = Mountain.objects.create(user=user, level=level, coords=coords, **validated_data)
        instance.save()

        for image_data in images_data:
            MountainImage.objects.create(mountain=instance, **image_data)
        return instance

    def update(self, instance, validated_data):
        if instance.status == 'NEW':
            if 'user' in validated_data:
                raise serializers.ValidationError('Update error. User fields are not changeable')

            if 'coords' in validated_data:
                coords = self.fields['coords']
                coords_instance = instance.coords
                coords_data = validated_data.pop('coords')
                coords.update(coords_instance, coords_data)

            if 'level' in validated_data:
                level = self.fields['level']
                level_instance = instance.level
                level_data = validated_data.pop('level')
                level.update(level_instance, level_data)

            if 'images' in validated_data:
                images_data = validated_data.pop('images')
                for image_data in images_data:
                    MountainImage.objects.update(mountain=instance, **image_data)

            return super(MountainSerializer, self).update(instance, validated_data)
        raise serializers.ValidationError('Update error. Object status is not <NEW>')
