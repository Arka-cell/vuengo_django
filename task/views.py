from django.shortcuts import render

from .models import Task
from .serializers import TaskSerializer

from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.response import Response

class TaskViewSet(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.all()
    def get(self, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = TaskSerializer(data=queryset, many=True)
        serializer.is_valid()
        return Response(serializer.data)