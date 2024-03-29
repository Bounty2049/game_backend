from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=128)
    question = models.TextField()
    image = models.ImageField(upload_to='media/questions/', default=None, null=True)
    is_true = models.BooleanField()


    def __str__(self):
        return self.title