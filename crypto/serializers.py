from rest_framework import serializers
from .models import VechainCandle


class VechainCandleSerializer(serializers.ModelSerializer):
    ''' VechainCandle Serializer
    
    '''
    def create(self, validated_data) -> dict:
        vechain = super().create(validated_data)
        vechain.save()

        return vechain

    class Meta:
        model = VechainCandle
        fields = ('__all__')

class BulkVechainCandleSerializer(serializers.ListSerializer):
    ''' VechainCandle Serializer for bulk-creating data

    '''
    child = VechainCandleSerializer() # required

    def create(self, validated_data):
        vechains = [VechainCandle(**data) for data in validated_data]
        return VechainCandle.objects.bulk_create(vechains)