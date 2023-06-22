from .models import Mountain, MountainImages, Coords, Author, Level
from rest_framework import serializers


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
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
        fields = ['title', 'image']


class MountainSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    level = LevelSerializer()
    coords = CoordsSerializer()
    images = ImageSerializer(source='mountain', many=True)

    class Meta:
        model = Mountain
        fields = ['title', 'other_title', 'author', 'level', 'coords', 'images']

    def create(self, validated_data):
        author_data = validated_data.pop('author')
        level_data = validated_data.pop('level')
        cords_data = validated_data.pop('coords')
        images_data = validated_data.pop('images')

        author = Author.objects.create(**author_data)
        level = Level.objects.create(**level_data)
        coords = Coords.objects.create(**cords_data)

        instance = Mountain.objects.create(author=author, level=level, coords=coords, **validated_data)
        instance.save()

        MountainImages.objects.create(mountain=instance, **images_data)
        return instance
