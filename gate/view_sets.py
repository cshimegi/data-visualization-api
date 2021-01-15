from rest_framework import viewsets
from . import models
from . import serializers

class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer

class UserLogViewSet(viewsets.ModelViewSet):
    queryset = models.UserLog.objects.all()
    serializer_class = serializers.UserLogSerializer