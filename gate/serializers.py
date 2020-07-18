from rest_framework import serializers
from . import models
import hashlib

class UserLogSerializer(serializers.ModelSerializer):
    class Meta:
        model  = models.UserLog
        fields = ('user', 'logged_time')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model  = models.User
        fields = ('id', 'name', 'email', 'password', 'authority')
        extra_kwargs = {
            'password'   : {'write_only': True}
        }
    
    def create(self, validated_data):
        return super().create(validated_data)