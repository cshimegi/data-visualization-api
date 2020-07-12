from rest_framework import viewsets
from . import models
from . import serializers

class UserLogViewSet(viewsets.ModelViewSet):
    queryset = models.UserLog.objects.all()
    serializer_class = serializers.UserLogSerializer
