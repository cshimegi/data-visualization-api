from django.db import models
from django.core.validators import validate_email, MinLengthValidator

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
    name       = models.CharField(max_length=32, unique=True)
    email      = models.EmailField(unique=True, validators=[validate_email])
    password   = models.CharField(validators=[MinLengthValidator(8)])
    authority  = models.SmallIntegerField(choices=USER_AUTH, default=GENERAL)
    updated_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now=True)

    # indexes
    class Meta:
        indexes = [
            models.Index(fields=['id'], name="idx_user_id"),
        ]
