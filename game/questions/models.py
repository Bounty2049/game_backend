from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=128)
    question = models.TextField()
    image = models.URLField(blank=True)
    is_true = models.BooleanField()


    def __str__(self):
        return self.title
    

class QuestionUsed(models.Model):
    question_id = models.IntegerField()