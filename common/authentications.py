from gate.models import User
from rest_framework.exceptions import ParseError, AuthenticationFailed
from rest_framework.authentication import BaseAuthentication
from rest_framework_jwt.settings import api_settings

from gate.models import User, UserLog
from gate.serializers import UserSerializer

JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER

class UserAuthentication(BaseAuthentication):
    def authenticate(self, request):
        username = request.data.get('name').strip()
        password = request.data.get('password').strip()

        if not all([username, password]):
            raise ParseError('User name and password are required!')
        
        user = User.objects.get_one_or_none(username = username)

        if not user or not user.do_check_password(password):
            raise AuthenticationFailed('Authentication is failed!')
        
        # Generate a token after successful login
        payload = JWT_PAYLOAD_HANDLER(user)
        token = JWT_ENCODE_HANDLER(payload)

        UserLog.objects.create(user = user, token = token)
        user_data = {
            'id': user.id,
            'name': user.username,
            'email': user.email,
            'authority': user.authority,
            'token': token
        }

        return (user_data, token)
    
    def authenticate_header(self, request):
        pass
