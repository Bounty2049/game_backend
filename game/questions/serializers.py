from rest_framework import serializers
from .models import Question, QuestionUsed


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class QuestionUsedSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionUsed
        fields = '__all__'