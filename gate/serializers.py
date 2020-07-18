from rest_framework import serializers
from . import models
from django.contrib.auth.hashers import make_password

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
        password = validated_data.get('password', None)
        
        if password is not None:
            validated_data['password'] = make_password(password)
        
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        instance.password = make_password(validated_data.get('password', instance.password))
        instance.save()

        return instance



