from django.db import models


class Guest(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=20)
    agreement = models.BooleanField()


    def __str__(self):
        return self.name