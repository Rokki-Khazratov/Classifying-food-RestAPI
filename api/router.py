from django.urls import path
from .views import *

urlpatterns = [

    path('images/', ImageModelListCreateView.as_view(), name="images"),
    path('images/<int:pk>', ImageModelRetrieveUpdateDestroyAPIView.as_view(), name="images-detail"),

]