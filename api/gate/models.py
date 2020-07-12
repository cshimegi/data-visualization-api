from django.db import models
from django.core.validators import (validate_email, validate_slug,
    MinLengthValidator, MaxLengthValidator)
from unixtimestampfield.fields import UnixTimeStampField
from model_utils.managers import QueryManager

# Create your models here.
class User(models.Model):
    # constants
    ADMIN     = 99
    GENERAL   = 1
    USER_AUTH = [
        (ADMIN, 'admin'),
        (GENERAL, 'general')
    ]

    # properties
    name         = models.CharField(
        max_length=32,
        unique=True,
        validators=[validate_slug]
    )
    email        = models.EmailField(unique=True, validators=[validate_email])
    password     = models.CharField(
        max_length=64,
        validators=[
            MinLengthValidator(8),
            MaxLengthValidator(64)
        ]
    )
    authority    = models.SmallIntegerField(choices=USER_AUTH, default=GENERAL)
    updated_time = UnixTimeStampField(auto_now_add=True)
    created_time = UnixTimeStampField(auto_now=True)

class UserLog(models.Model):
    # properties
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    logged_time = UnixTimeStampField(db_index=True, auto_now_add=True)

    # indexes
    class Meta:
        indexes = [
            models.Index(fields=['logged_time'], name="idx_user_log_logged_time"),
        ]