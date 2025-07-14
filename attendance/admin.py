from django.contrib import admin
from .models import Attendance, AttendanceRecord

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'check_in', 'check_out')
    list_filter = ('date',)

class AttendanceRecordAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'status')  # shows these columns
    list_filter = ('status', 'date')           # adds filters on right side
    search_fields = ('user__username',)        # adds a search bar for username

admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(AttendanceRecord, AttendanceRecordAdmin)
