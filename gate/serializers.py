from rest_framework import serializers
from . import models
from django.contrib.auth.hashers import make_password
import json

class UserLogSerializer(serializers.ModelSerializer):
    class Meta:
        model  = models.UserLog
        fields = ('__all__')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model  = models.User
        fields = ('id', 'name', 'email', 'password', 'authority')
        extra_kwargs = {
            'password'   : {'write_only': True, 'required': False}
        }
    
    def create(self, validated_data):
        password = validated_data.get('password', None)
        
        if password is not None:
            validated_data['password'] = make_password(password)
        else:
            detail = {"password": ["This field may not be blank."]}
            raise serializers.ValidationError(detail=detail)
        
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        password = validated_data.get('password', None)
        
        validated_data['password'] = instance.password if password is None else make_password(password)

        return super().update(instance, validated_data)



