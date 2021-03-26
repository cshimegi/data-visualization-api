from django.contrib import admin
from .models import Calendar
from datetime import datetime

DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'
# Register your models here.
class CalendarAdmin(admin.ModelAdmin):
    list_display = ('user', 'label', 'detail', 'view_updated_time', 'view_created_time')
    list_display_links = None

    def view_updated_time(self, obj):
        return datetime.fromtimestamp(obj.updated_time).strftime(DATETIME_FORMAT)
    
    def view_created_time(self, obj):
        return datetime.fromtimestamp(obj.created_time).strftime(DATETIME_FORMAT)

admin.site.register(Calendar, CalendarAdmin)