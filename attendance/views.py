from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Attendance
from .serializers import AttendanceSerializer
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import AttendanceRecord
from django.shortcuts import render, redirect
from .forms import AttendanceForm
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

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
        form = AttendanceForm(request.POST)
        if form.is_valid():
            attendance = form.save(commit=False)
            attendance.user = request.user
            attendance.save()
            return redirect('mark_attendance')  # or a success page
    else:
        form = AttendanceForm()
    return render(request, 'attendance/mark_attendance.html', {'form': form})

@login_required
def attendance_history(request):
    start_date = request.GET.get('start')
    end_date = request.GET.get('end')
    records = AttendanceRecord.objects.filter(user=request.user)
    if start_date and end_date:
        records = records.filter(date__range=[start_date, end_date])
    return render(request, 'attendance/attendance_history.html', {'records': records})

@login_required
def download_attendance_pdf(request):
    records = AttendanceRecord.objects.filter(user=request.user).order_by('-date')
    template = get_template('attendance/attendance_pdf.html')
    html = template.render({'records': records, 'user': request.user})
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="attendance_history.pdf"'
    
    pisa.CreatePDF(html, dest=response)
    return response

def attendance_home(request):
    return HttpResponse("Welcome to the home page")

# Make sure 'users' is in INSTALLED_APPS in your settings.py
# Example:
# INSTALLED_APPS = [
#     ...existing apps...
#     'users',
#     ...existing apps...
# ]
# ]
