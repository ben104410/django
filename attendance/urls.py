from django.urls import path
from . import views

urlpatterns = [
    path("mark/", views.mark_attendance, name="mark_attendance"),
    path("history/", views.attendance_history, name="attendance_history"),
    path("download-pdf/", views.download_attendance_pdf, name="download_attendance_pdf"),
]
