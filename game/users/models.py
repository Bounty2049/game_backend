from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone = models.CharField(max_length=30, blank=True, null=False)

    REQUIRED_FIELDS = ['email', 'phone']

    def __str__(self):
        return self.username