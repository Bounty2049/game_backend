from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('api/', views.UserView.as_view(), name='api'),
    path('api/reg/', views.registration, name='registration')
]