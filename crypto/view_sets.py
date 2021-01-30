from rest_framework import viewsets
from .models import VechainCandle
from .serializers import VechainCandleSerializer

class VechainCandleViewSet(viewsets.ModelViewSet):
    queryset = VechainCandle.objects.all()
    serializer_class = VechainCandleSerializer

    def get_queryset(self):
        ''' @override super().get_queryset

        '''
        from_date = self.request.query_params.get('fromDate', None)
        
        if from_date:
            return self.queryset.filter(period__gte = from_date)
        else:
            return self.queryset