from rest_framework import viewsets, status
from .models import Calendar
from .serializers import CreateCalendarSerializer, CalendarSerializer
from common.authentications import get_user
from rest_framework.response import Response

class CalendarViewSet(viewsets.ModelViewSet):
    queryset = Calendar.objects.all()

    def create(self, request, *args, **kwargs):
        ''' @override

        '''
        request.data.update({'user': get_user(request)})

        serializer = self.get_serializer(data = request.data)

        serializer.is_valid(raise_exception = True)
        self.perform_create(serializer)
        
        headers = self.get_success_headers(serializer.data)
        
        return Response(
            serializer.data,
            status = status.HTTP_200_OK,
            headers = headers
        )
    
    def list(self, request, *args, **kwargs):
        ''' @override

        '''
        user_id = get_user(request)

        if not user_id:
            return Response(
                None,
                status = status.HTTP_401_UNAUTHORIZED
            )

        queryset = self.queryset.filter(user_id = user_id)
        serializer = self.get_serializer(queryset, many=True)

        return Response(
            serializer.data,
            status = status.HTTP_200_OK
        )

    def get_serializer_class(self):
        ''' @override

        '''
        is_cu = (self.action == 'create' or self.action == 'update')

        return CreateCalendarSerializer if is_cu else CalendarSerializer