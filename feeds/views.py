# feeds/views.py
from rest_framework import generics

from feeds import models
from . import serializers


class ListFeed(generics.ListCreateAPIView):
    queryset = models.Feed.objects.all()
    serializer_class = serializers.TodoSerializer


class DetailFeed(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Feed.objects.all()
    serializer_class = serializers.TodoSerializer
