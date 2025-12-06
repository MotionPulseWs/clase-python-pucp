from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class profileSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(read_only=True)
    age = serializers.IntegerField(read_only=True)

    class Meta:
        model = Profile
        fields = ['bio', 'avatar', 'birthdate', 'full_name', 'edad', 'is_private']

class UserSerializer(serializers.ModelSerializer):
    profile = profileSerializer(read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'profile']