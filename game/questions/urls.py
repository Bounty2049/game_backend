from django.urls import path

from . import views

app_name = 'questions'


urlpatterns = [
    path('api/', views.QuestionViewSet.as_view(), name='api')
]