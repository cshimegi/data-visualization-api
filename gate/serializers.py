from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
    ''' User Information

    '''

    class Meta:
        from django.conf import settings

        model  = models.User
        fields = ('id', 'username', 'email', 'password', 'authority')

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
        
        return attrs
    
    def __validate_password(self, password: str, confirmed_password: str) -> bool:
        '''Validate if plain password matches
        
        Args:
            password (str): user's password
            confirmed_password (str): password for checking if password is desirable
        
        Returns:
            The return value. True if same, False otherwise
        '''
        return password == confirmed_password

    def create(self, validated_data) -> dict:
        '''Create user

        Args:
            validated_data (dict): validated user's required information
        '''
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
        fields = ('username', 'email', 'password', 'confirmed_password', 'authority')

class PartialUserSerializer(serializers.ModelSerializer):
    ''' Partial User Information

    '''
    class Meta:
        model  = models.User
        fields = ('id', 'username', 'email', 'authority')

class UserLogSerializer(serializers.ModelSerializer):
    ''' User log information

    '''
    user = PartialUserSerializer(read_only=True) # get joining table's data

    class Meta:
        model  = models.UserLog
        fields = ('id', 'user', 'logged_time')

class CreateUserLogSerializer(serializers.ModelSerializer):
    ''' User log information

    '''
    def create(self, data) -> dict:
        user_log = super().create(data)
        user_log.save()
        
        return user_log

    class Meta:
        model  = models.UserLog
        fields = ('__all__')