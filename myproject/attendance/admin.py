from django.contrib import admin
from .models import Attendance

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('user', 'check_in', 'check_out', 'status')
    list_filter = ('user', 'check_in', 'status')
