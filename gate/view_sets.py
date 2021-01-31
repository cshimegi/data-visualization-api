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

    def get_queryset(self):
        ''' @override

        '''
        from_date = self.request.query_params.get('fromDate', None)
        order = self.request.query_params.get('order', 'asc')
        order_by = self.request.query_params.get('orderBy', 'id')

        if order_by == 'loggedTime':
            order_by = 'logged_time'
        elif order_by == 'username' or order_by == 'authority':
            order_by = 'user__' + order_by # format for related object's field

        if order == 'desc':
            order_by = '-' + order_by
        
        if from_date:
            return self.queryset.filter(logged_time__gte = from_date).order_by(order_by)
        else:
            return self.queryset.order_by(order_by)