from rest_framework import serializers
from .models import User, UserLog

class UserSerializer(serializers.ModelSerializer):
    ''' User Information

    '''
    class Meta:
        model  = User
        fields = ('id', 'username', 'email', 'password', 'is_staff', 'is_superuser')
    
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.is_staff = validated_data.get('is_staff', instance.is_staff)
        instance.is_superuser = validated_data.get('is_superuser', instance.is_superuser)
        
        if validated_data.get('password', instance.password) != instance.password:
            instance.set_password(validated_data.get('password', instance.password))
        
        instance.save()

        return instance

class CreateUserSerializer(serializers.ModelSerializer):
    ''' Create User Serializer
    
    '''
    confirmed_password = serializers.CharField(
        max_length = User.MAX_PASSWORD_LENGTH,
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
        model = User
        confirmed_password = serializers.CharField(
            max_length = User.MAX_PASSWORD_LENGTH,
            write_only = True
        )
        fields = ('username', 'email', 'password', 'confirmed_password', 'is_staff', 'is_superuser')

class PartialUserSerializer(serializers.ModelSerializer):
    ''' Partial User Information

    '''
    class Meta:
        model  = User
        fields = ('id', 'username', 'email', 'is_staff')

class UserLogSerializer(serializers.ModelSerializer):
    ''' User log information

    '''
    user = PartialUserSerializer(read_only=True) # get joining table's data

    class Meta:
        model  = UserLog
        fields = ('id', 'user', 'logged_time')

class CreateUserLogSerializer(serializers.ModelSerializer):
    ''' User log information

    '''
    def create(self, data) -> dict:
        user_log = super().create(data)
        user_log.save()
        
        return user_log

    class Meta:
        model  = UserLog
        fields = ('__all__')