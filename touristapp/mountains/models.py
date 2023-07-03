from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(null=False, blank=False)
    phone = models.CharField(max_length=12, null=False, blank=False)


class Level(models.Model):
    winter = models.CharField(max_length=2, blank=True)
    summer = models.CharField(max_length=2, blank=True)
    autumn = models.CharField(max_length=2, blank=True)
    spring = models.CharField(max_length=2, blank=True)


class Coord(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.IntegerField()


class Mountain(models.Model):
    NEW = 'NEW'
    PEN = 'PEN'
    ACC = 'ACC'
    REJ = 'REJ'

    STATUS = [
        (NEW, 'new'),
        (PEN, 'pending'),
        (ACC, 'accepted'),
        (REJ, 'rejected')
    ]

    beauty_title = models.CharField(max_length=255, blank=True)
    title = models.CharField(max_length=255)
    other_title = models.CharField(max_length=255, blank=True)
    connect = models.CharField(max_length=255, blank=True)
    add_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coords = models.ForeignKey(Coord, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    status = models.CharField(max_length=3, choices=STATUS, default=NEW)


class MountainImage(models.Model):
    mountain = models.ForeignKey(Mountain, on_delete=models.CASCADE, related_name='images')
    data = models.URLField()
    title = models.CharField(max_length=255)
