from rest_framework import serializers
from . import models

class UserLogSerializer(serializers.ModelSerializer):
    ''' User log information

    '''
    class Meta:
        model  = models.UserLog
        fields = ('__all__')

class UserSerializer(serializers.ModelSerializer):
    ''' User Information

    '''

    class Meta:
        from django.conf import settings

        model  = models.User
        fields = ('id', 'name', 'email', 'password', 'authority')

        if not settings.DEBUG:
            extra_kwargs = {
                'password': {'write_only': True}
            }
    

        
class CreateUserSerializer(serializers.ModelSerializer):
    ''' Create User Serializer
    
    '''
    confirmed_password = serializers.CharField(
        max_length = models.User.MAX_PASSWORD_LENGTH,
        write_only = True
    )

    def validate(self, attrs) -> dict:
        if not self.__validate_password(attrs['password'], attrs['confirmed_password']):
            raise serializers.ValidationError('The two passwords are inconsistent, please re-enter!')
        
        self.__validate_email(attrs['email'])
        
        return attrs
    
    def __validate_password(self, password, confirmed_password) -> bool:
        ''' validate if plain password matches
        
        '''
        return password == confirmed_password

    def __validate_email(self, email) -> None:
        ''' validate email format

        '''
        from django.core.validators import validate_email
        
        try:
            validate_email(email)
        except validate_email.ValidationError:
            # ToDo: log system
            pass
 
    def create(self, validated_data) -> dict:
        del validated_data['confirmed_password']
        
        user = super().create(validated_data)
        
        user.set_password(validated_data['password'])
        user.save()
        
        return user
 
    class Meta:
        model = models.User
        confirmed_password = serializers.CharField(
            max_length = models.User.MAX_PASSWORD_LENGTH,
            write_only = True
        )
        fields = ('name', 'email', 'password', 'confirmed_password', 'authority')


