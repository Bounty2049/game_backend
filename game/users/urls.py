from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('api/', views.GuestView.as_view(), name='api'),
    path('api/to_excel/', views.ExportToExcel.as_view(), name='export to excel'),
    path('api/to_csv/', views.ExportToCSV.as_view(), name='export to csv')
]