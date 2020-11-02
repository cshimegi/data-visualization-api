from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView
from django.http import JsonResponse, HttpResponseBadRequest
from rest_framework.views import APIView
from rest_framework import status
 
from . import models, serializers
 
class UserLoginView(APIView):
    ''' User login view class

    '''
    authentication_classes = []
    # Login does not require authentication
    def post(self, request):
        name = request.data.get('name').strip()
        password = request.data.get('password').strip()
        
        if not all([name, password]):
            return HttpResponseBadRequest('User name and password are required!')
        
        if not models.User.objects.filter(name = name).exists():
            return HttpResponseBadRequest('User name is not existed!')
        
        user = models.User.objects.get(name = name)

        if not user.do_check_password(password):
            return HttpResponseBadRequest('Password is wrong!')
        
        # Generate a token after successful login
        token = 'adasdsadasdas'

        # Todo: models.UserToken.objects.update_or_create(user=user,defaults={'token':token})
        result = serializers.UserSerializer(user).data
        result['token'] = token

        return JsonResponse({'code': status.HTTP_200_OK, 'user': result})

class UserRegisterView(CreateAPIView):
    '''User Registration View
    
    '''
    authentication_classes = []
    #User registration does not require authentication
    serializer_class = serializers.CreateUserSerializer
