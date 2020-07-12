from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model  = models.User
        fields = ('id', 'name')

class UserLogSerializer(serializers.ModelSerializer):
    class Meta:
        model  = models.UserLog
        fields = (models.User, 'logged_time')