from django.db import models
from django.core.validators import (validate_email, validate_slug,
    MinLengthValidator, MaxLengthValidator)
from unixtimestampfield.fields import UnixTimeStampField
from django.contrib.auth.hashers import make_password, check_password
from .managers import ModelManager

# Create your models here.
class User(models.Model):
    # constants
    ADMIN     = 99
    GENERAL   = 1
    USER_AUTH = [
        (ADMIN, 'admin'),
        (GENERAL, 'general')
    ]
    MAX_NAME_LENGTH = 32
    MIN_PASSWORD_LENGTH = 8
    MAX_PASSWORD_LENGTH = 512
    PASSWORD_SALT= 'alan-data-science-web-app'

    # properties
    username       = models.CharField(
        max_length = MAX_NAME_LENGTH,
        unique = True,
        validators = [validate_slug]
    )
    email        = models.EmailField(unique = True, validators = [validate_email])
    password     = models.CharField(
        max_length = MAX_PASSWORD_LENGTH,
        validators = [
            MinLengthValidator(MIN_PASSWORD_LENGTH),
            MaxLengthValidator(MAX_PASSWORD_LENGTH)
        ]
    )
    authority    = models.SmallIntegerField(choices = USER_AUTH, default = GENERAL)
    updated_time = UnixTimeStampField(auto_now_add = True)
    created_time = UnixTimeStampField(auto_now = True)
    objects = ModelManager()

    class Meta:
        verbose_name = 'user information table'
        verbose_name_plural = verbose_name
        ordering = ['-authority']
    
    def __str__(self) -> str:
        return self.username
    
    def set_password(self, password) -> None:
        self.password = make_password(password, salt = self.PASSWORD_SALT)
    
    def do_check_password(self, password) -> bool:
        return check_password(password, self.password)

class UserLog(models.Model):
    # constants
    MAX_TOKEN_LENGTH = 512

    # properties
    user        = models.ForeignKey(User, to_field = 'id', on_delete = models.CASCADE, related_name = "user_id")
    token       = models.CharField(max_length = MAX_TOKEN_LENGTH, null = True)
    logged_time = UnixTimeStampField(db_index = True, auto_now_add = True)

    # indexes
    class Meta:
        verbose_name = 'user log information'
        verbose_name_plural = verbose_name
        indexes = [
            models.Index(fields = ['logged_time'], name = "idx_user_log_logged_time"),
        ]
        ordering = ['-logged_time']