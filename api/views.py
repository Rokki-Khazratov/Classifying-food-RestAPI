from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser


from .serializers import ImageModelSerializer
from api.models import ImageModel

class ImageModelListCreateView(generics.ListCreateAPIView):
    queryset = ImageModel.objects.all()
    serializer_class = ImageModelSerializer


class ImageModelRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ImageModel.objects.all()
    serializer_class = ImageModelSerializer



class ImageModelAPIView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        serializer = ImageModelSerializer(data=request.data)

        if serializer.is_valid():
            instance = serializer.save()

            return Response(ImageModelSerializer(instance).data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)