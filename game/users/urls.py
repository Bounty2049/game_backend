from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('api/', views.GuestView.as_view(), name='api'),
]