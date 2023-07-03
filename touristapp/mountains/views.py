from rest_framework import viewsets, status
from rest_framework.response import Response
from django_filters import rest_framework

from .serializers import MountainSerializer
from .models import Mountain


class MountainsViewset(viewsets.ModelViewSet):
    queryset = Mountain.objects.all()
    serializer_class = MountainSerializer
    filter_backends = [rest_framework.DjangoFilterBackend]
    filterset_fields = ['user__email']
    http_method_names = ['get', 'post', 'patch', 'delete', 'head', 'options']

    def create(self, request, *args, **kwargs):
        serializer = MountainSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': 200,
                'message': 'The record was successfully added to the database',
                'id': serializer.data['id'],
            })

        if status.HTTP_400_BAD_REQUEST:
            return Response({
                'status': 400,
                'message': 'Bad request',
                'id': None,
            })

        if status.HTTP_500_INTERNAL_SERVER_ERROR:
            return Response({
                'status': 500,
                'message': 'Error connecting to database',
                'id': None,
            })

    def partial_update(self, request, *args, **kwargs):
        mountain = self.get_object()
        serializer = self.get_serializer(mountain, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'state': 1,
                'message': 'The record was successfully updated'
            })

        else:
            return Response({
                'state': 0,
                'message': serializer.errors
            })
