from rest_framework import routers
from .views import MountainsViewset
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'submitdata', MountainsViewset, basename='submitdata')

urlpatterns = [
    path('', include(router.urls)),
]