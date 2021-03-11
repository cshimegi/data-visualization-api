from django.db import models
from gate.models import User
from django.core.validators import (validate_slug, MaxLengthValidator)
from unixtimestampfield.fields import UnixTimeStampField

# Create your models here.
class Calendar(models.Model):
    # constants
    MAX_LABEL_LENGTH = 64

    # properties
    user = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = "calendars"
    )
    label = models.CharField(
        max_length = MAX_LABEL_LENGTH,
        validators = [
            validate_slug,
            MaxLengthValidator(MAX_LABEL_LENGTH)
        ]
    )
    detail         = models.TextField(blank = True, null = True)
    triage         = models.SmallIntegerField()
    do_remind      = models.BooleanField(default = False)
    remind_minutes = models.SmallIntegerField()
    from_time      = UnixTimeStampField(use_numeric = True)
    to_time        = UnixTimeStampField(use_numeric = True)
    updated_time   = UnixTimeStampField(auto_now_add = True, use_numeric = True)
    created_time   = UnixTimeStampField(auto_now = True, use_numeric = True)

    class Meta:
        verbose_name = 'user calendar table'
        verbose_name_plural = verbose_name
        ordering = ['from_time']