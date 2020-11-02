from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
 
from . import models, serializers
 
class UserLoginView(APIView):
    ''' User login view class

    '''
    authentication_classes = []
    # Login does not require authentication
    def post(self, request) -> Response:
        name = request.POST.get('name').strip()
        password = request.POST.get('password').strip()
        
        if not all([name, password]):
            return Response({
                'info': 'User name and password are required!',
                'code': status.HTTP_400_BAD_REQUEST
            })
        
        user = models.User.objects.get(name = name)

        if not user.do_check_password(password):
            return Response({
                'error': 'The user is not existed!',
                'code': status.HTTP_401_UNAUTHORIZED
            })
        
        # Generate a token after successful login
        token = 'adasdsadasdas'

        # models.UserToken.objects.update_or_create(user=user,defaults={'token':token})
        # result = {'info':'success', 'token':token, 'code':200}
        # result['data'] = ser.UserInfoSer(user).data
        
        return Response({
            'info': 'Success',
            'token': token,
            'code': status.HTTP_200_OK,
            'data': serializers.UserSerializer(user).data
        })

class UserRegisterView(CreateAPIView):
    '''User Registration View
    
    '''
    authentication_classes = []
    #User registration does not require authentication
    serializer_class = serializers.CreateUserSerializer
