from rest_framework import viewsets
from .models import VechainCandle
from . import serializers

class VechainCandleViewSet(viewsets.ModelViewSet):
    queryset = VechainCandle.objects.all()
    serializer_class = serializers.VechainCandleSerializer