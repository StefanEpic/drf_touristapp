from .models import Mountain, MountainImage, Coord, User, Level
from rest_framework import serializers


# from drf_writable_nested.serializers import WritableNestedModelSerializer


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
    id = serializers.IntegerField(required=False)

    class Meta:
        model = MountainImage
        fields = ['id', 'data', 'title']


class MountainSerializer(serializers.ModelSerializer):
    user = UsersSerializer()
    coords = CoordsSerializer()
    level = LevelSerializer()
    images = ImageSerializer(many=True)

    class Meta:
        model = Mountain
        fields = ['id', 'beauty_title', 'title', 'other_title', 'connect', 'add_time', 'user', 'coords', 'level',
                  'images', 'status']
        read_only_fields = ['id', 'status', 'add_time']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        cords_data = validated_data.pop('coords')
        level_data = validated_data.pop('level')
        images_data = validated_data.pop('images')

        user_email = user_data.get('email')
        if User.objects.filter(email=user_email).exists():
            user = User.objects.get(email=user_email)

        else:
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

                # if "id" is passed - the image is updated, otherwise it is added
                for image in images_data:
                    image_id = image.get('id', None)
                    if image_id:
                        inv_image = MountainImage.objects.get(id=image_id)
                        inv_image.data = image.get('data', inv_image.data)
                        inv_image.title = image.get('title', inv_image.title)
                        inv_image.save()
                    else:
                        MountainImage.objects.create(mountain=instance, **image)

                # clear list images
                images_dict = dict((i.id, i) for i in instance.images.all())
                if len(images_data) == 0:
                    for image in images_dict.values():
                        image.delete()

            return super(MountainSerializer, self).update(instance, validated_data)
        raise serializers.ValidationError('Update error. Object status is not <NEW>')
