from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, null=False, blank=False)
    phone = PhoneNumberField(unique=True, null=False, blank=False)


class Level(models.Model):
    winter = models.CharField(max_length=2, blank=True)
    summer = models.CharField(max_length=2, blank=True)
    autumn = models.CharField(max_length=2, blank=True)
    spring = models.CharField(max_length=2, blank=True)


class Coords(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.IntegerField()


class Mountain(models.Model):
    STATUS = [
        ('NEW', 'new'),
        ('PEN', 'pending'),
        ('ACC', 'accepted'),
        ('REJ', 'rejected')
    ]

    title = models.CharField(max_length=255)
    other_title = models.CharField(max_length=255, blank=True)
    add_time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    coords = models.ForeignKey(Coords, on_delete=models.CASCADE)
    status = models.CharField(max_length=3, choices=STATUS, default='NEW')


class MountainImages(models.Model):
    mountain = models.ForeignKey(Mountain, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='mountain_images/%Y/%m/%d/')
