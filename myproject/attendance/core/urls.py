from django.urls import path
from . import views

urlpatterns = [
    path('', views.attendance_home, name='attendance_home'),
    path('mark/', views.mark_attendance, name='mark_attendance'),
]