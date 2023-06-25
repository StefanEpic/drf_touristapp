from rest_framework import viewsets
from django_filters import rest_framework

from .serializers import MountainSerializer
from .models import Mountain


class MountainsViewset(viewsets.ModelViewSet):
    queryset = Mountain.objects.all()
    serializer_class = MountainSerializer
    filter_backends = [rest_framework.DjangoFilterBackend]
    filterset_fields = ['user__email']
