from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, UserLog

DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'

# Register your models here.
class UserLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'view_logged_time')
    list_display_links = None

    def view_logged_time(self, obj):
        return obj.logged_time.strftime(DATETIME_FORMAT)

admin.site.register(User, UserAdmin)
admin.site.register(UserLog, UserLogAdmin)