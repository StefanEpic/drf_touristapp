from .models import Mountain, MountainImages, Coords, Users, Level
from rest_framework import serializers


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['first_name', 'second_name', 'last_name', 'email', 'phone']


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ['winter', 'summer', 'autumn', 'spring']


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = ['latitude', 'longitude', 'height']


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MountainImages
        fields = ['data', 'title']


class MountainSerializer(serializers.ModelSerializer):
    author = UsersSerializer()
    level = LevelSerializer()
    coords = CoordsSerializer()
    images = ImageSerializer(many=True)

    class Meta:
        model = Mountain
        fields = ['beauty_title', 'title', 'other_title', 'connect', 'add_time', 'author', 'level', 'coords', 'images', 'status']
        read_only_fields = ['pk', 'status', 'add_time']


    def create(self, validated_data):
        author_data = validated_data.pop('author')
        level_data = validated_data.pop('level')
        cords_data = validated_data.pop('coords')
        images_data = validated_data.pop('images')

        author = Users.objects.create(**author_data)
        level = Level.objects.create(**level_data)
        coords = Coords.objects.create(**cords_data)

        instance = Mountain.objects.create(author=author, level=level, coords=coords, **validated_data)
        instance.save()

        for image_data in images_data:
            MountainImages.objects.create(mountain=instance, **image_data)
        return instance
