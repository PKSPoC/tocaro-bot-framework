from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializer import CommandSerializer
from .models import Command


class CommandViewSet(ModelViewSet):
    authentication_classes = []
    queryset = Command.objects.all()
    serializer_class = CommandSerializer
