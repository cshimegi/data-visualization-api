from rest_framework import viewsets
from .models import User, UserLog
from .serializers import UserSerializer, UserLogSerializer
from .paginations import UserPagination, UserLogPagination

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = UserPagination

class UserLogViewSet(viewsets.ModelViewSet):
    queryset = UserLog.objects.all()
    serializer_class = UserLogSerializer
    pagination_class = UserLogPagination