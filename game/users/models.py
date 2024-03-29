from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone = models.CharField(max_length=30, blank=False, null=False)
    email = models.EmailField(unique=True, blank=False, null=False)
    username = models.CharField(max_length=100, unique=False)

    REQUIRED_FIELDS = ['phone', 'username']
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.username