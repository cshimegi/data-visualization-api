from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView
from django.http import JsonResponse, HttpResponseBadRequest
from rest_framework.views import APIView
from rest_framework import status
from common.authentications import UserAuthentication

from . import models, serializers

class UserLoginView(APIView):
    ''' User login view class

    '''
    authentication_classes = [UserAuthentication]
    # Login does not require authentication
    def post(self, request):
        return JsonResponse({'code': status.HTTP_200_OK, 'user': request.user})

class UserRegisterView(CreateAPIView):
    '''User Registration View
    
    '''
    authentication_classes = []
    #User registration does not require authentication
    serializer_class = serializers.CreateUserSerializer
