from rest_framework import serializers
from .models import User, Quote, Command


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "name", "email")


class QuoteSerializer(serializers.ModelSerializer):
    #author = UserSerializer()

    class Meta:
        model = Quote
        fields = ("id", "quote", "author", "status", "created_at")


class CommandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Command
        fields = ("id", "command")
