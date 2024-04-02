from django.urls import path

from . import views

app_name = 'questions'


urlpatterns = [
    path('api/', views.QuestionViewSet.as_view(), name='api'),
    path('api/<int:pk>/', views.QuesetionRetrieve.as_view(), name='api-details'),
    path('api/used/', views.QuestionUsedView.as_view(), name='array-of-used-questions')
]