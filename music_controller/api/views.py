from django.shortcuts import render
from rest_framework import generics

# Create your views here.
from .serializers import RoomSerializer
from .models import Room


class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
