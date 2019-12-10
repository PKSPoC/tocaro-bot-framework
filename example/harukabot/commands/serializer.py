from .models import Command
from rest_framework import serializers


class CommandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Command
        fields = ("id", "command")
