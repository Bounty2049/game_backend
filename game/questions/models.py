from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=128)
    question = models.TextField()
    is_true = models.BooleanField()


    def __str__(self):
        return self.title