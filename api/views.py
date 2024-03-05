from rest_framework import generics

from .serializers import ImageModelSerializer
from api.models import ImageModel

class ImageModelListCreateView(generics.ListCreateAPIView):
    queryset = ImageModel.objects.all()
    serializer_class = ImageModelSerializer


class ImageModelRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ImageModel.objects.all()
    serializer_class = ImageModelSerializer