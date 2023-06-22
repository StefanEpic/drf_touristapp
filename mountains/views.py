from django.contrib.auth.models import User
from rest_framework import viewsets

from .serializers import MountainSerializer
from .models import Mountain


class MountainsViewset(viewsets.ModelViewSet):
    queryset = Mountain.objects.all()
    serializer_class = MountainSerializer
