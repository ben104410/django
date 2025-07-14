from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from attendance.models import Attendance
from attendance.serializers import AttendanceSerializer
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from functools import wraps
# from users.decorators import staff_required

@api_view(['POST'])
def check_in(request):
    user_id = request.data.get('user')
    try:
        user = User.objects.get(id=user_id)
        attendance = Attendance.objects.create(user=user, check_in=timezone.now(), status='Present')
        serializer = AttendanceSerializer(attendance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def check_out(request):
    user_id = request.data.get('user')
    try:
        user = User.objects.get(id=user_id)
        attendance = Attendance.objects.filter(user=user).latest('check_in')
        attendance.check_out = timezone.now()
        attendance.save()
        serializer = AttendanceSerializer(attendance)
        return Response(serializer.data)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    except Attendance.DoesNotExist:
        return Response({"error": "No check-in found for user"}, status=status.HTTP_404_NOT_FOUND)

@login_required
def mark_attendance(request):
    if request.method == 'POST':
        Attendance.objects.create(user=request.user)
        return render(request, 'attendance/thank_you.html')
    return render(request, 'attendance/mark_attendance.html')
    return render(request, 'attendance/mark_attendance.html')

def dashboard_view(request):
    # Example dummy data, replace with your actual model queries
    attendance_records = [
        {'student_name': 'Alice', 'status': 'Present', 'date': '2025-06-27'},
        {'student_name': 'Bob', 'status': 'Absent', 'date': '2025-06-27'},
    ]
    context = {
        'total_present': 1,
        'total_absent': 1,
        'attendance_records': attendance_records,
    }
    return render(request, 'attendance/dashboard.html', context)

def attendance_home(request):
    return render(request, 'attendance/home.html')

@staff_member_required
def staff_dashboard(request):
    # logic to show staff dashboard
    return render(request, 'attendance/staff_dashboard.html')

# Make sure you run Django commands from the project root where manage.py is located:
# C:\Users\ADMIN\Desktop\project\myproject
# and your settings module is 'myproject.settings'

# If you still get "No module named 'myproject.settings'", check:
# 1. The folder structure:
#    C:\Users\ADMIN\Desktop\project\myproject\manage.py
#    C:\Users\ADMIN\Desktop\project\myproject\myproject\settings.py
# 2. That you run commands like:
#    python manage.py migrate
