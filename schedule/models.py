from django.db import models
from gate.models import User
from django.core.validators import (validate_slug, MaxLengthValidator)
from unixtimestampfield.fields import UnixTimeStampField

# Create your models here.
class Calendar(models.Model):
    # constants
    MAX_LABEL_LENGTH = 64
    BLACK  = 4
    GREEN  = 3
    ORANGE = 2
    RED    = 1
    TRIAGES = [
        (BLACK, 'black'),
        (GREEN, 'green'),
        (ORANGE, 'orange'),
        (RED, 'red')
    ]
    NO_REMIND = 0
    TEN_MINS = 10
    ONE_QUARTER = 15
    HALF_HOUR = 30
    THREE_QUARTERS = 45
    ONE_HOUR = 60
    REMIND_MINUTES = [
        (NO_REMIND, 'No remind'),
        (TEN_MINS, '10 minutes'),
        (ONE_QUARTER, '15 minutes'),
        (HALF_HOUR, '30 minutes'),
        (THREE_QUARTERS, '45 minutes'),
        (ONE_HOUR, '60 minutes')
    ]

    # properties
    user = models.ForeignKey(
        User,
        to_field = 'id',
        on_delete = models.CASCADE,
        related_name = "calendar_user_id"
    )
    label = models.CharField(
        max_length = MAX_LABEL_LENGTH,
        validators = [
            validate_slug,
            MaxLengthValidator(MAX_LABEL_LENGTH)
        ]
    )
    detail         = models.TextField(blank = True, null = True)
    triage         = models.SmallIntegerField(default = BLACK, choices = TRIAGES)
    do_remind      = models.BooleanField(default = False)
    remind_minutes = models.SmallIntegerField(default = NO_REMIND, choices = REMIND_MINUTES)
    from_time      = UnixTimeStampField(use_numeric = True)
    to_time        = UnixTimeStampField(use_numeric = True)
    updated_time   = UnixTimeStampField(auto_now_add = True, use_numeric = True)
    created_time   = UnixTimeStampField(auto_now = True, use_numeric = True)

    class Meta:
        verbose_name = 'user calendar table'
        verbose_name_plural = verbose_name
        ordering = ['from_time']