from rest_framework import serializers
from .models import Calendar
from gate.models import User
from django.utils.html import escape


class CalendarUserSerializer(serializers.ModelSerializer):
    ''' Calendar User Information

    '''
    class Meta:
        model  = User
        fields = ('id', 'username', 'email')

class CalendarSerializer(serializers.ModelSerializer):
    ''' User Calendar information

    '''
    user = CalendarUserSerializer(read_only = True) # get joining table's data

    class Meta:
        model  = Calendar
        fields = ('id', 'user', 'label', 'detail', 'triage', 'do_remind', 'remind_minutes', 'from_time', 'to_time')

class CreateCalendarSerializer(serializers.ModelSerializer):
    ''' User Calendar information

    '''
    user = serializers.PrimaryKeyRelatedField(queryset = User.objects.all())

    class Meta:
        model  = Calendar
        fields = ('id', 'user', 'label', 'detail', 'triage', 'do_remind', 'remind_minutes', 'from_time', 'to_time')
    
    def validate_detail(self, value):
        if value:
            return escape(value)