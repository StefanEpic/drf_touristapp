from .models import Mountain, MountainImages, Coords, Author, Level
from rest_framework import serializers


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = "__all__"


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = "__all__"


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MountainImages
        fields = ['data', 'title']


class MountainSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    level = LevelSerializer()
    coords = CoordsSerializer()
    images = ImageSerializer(many=True, required=False)

    class Meta:
        model = Mountain
        fields = ['title', 'other_title', 'add_time', 'author', 'level', 'coords', 'images', 'status']
        read_only_fields = ['pk', 'status', 'add_time']
        depth = 1

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

        for image_data in images_data:
            MountainImages.objects.create(mountain=instance, **image_data)
        return instance
