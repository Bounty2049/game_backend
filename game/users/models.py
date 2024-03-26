from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone = models.CharField(max_length=30, blank=True, null=False)

    def __str__(self):
        return self.username