from django.http import HttpResponse
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect

def users_home(request):
    return HttpResponse("Welcome to the Users homepage!")

def redirect_to_login(request):
    return redirect('login')

def login_view(request, *args, **kwargs):
    return auth_views.LoginView.as_view(template_name='registration/login.html')(request, *args, **kwargs)

def logout_view(request, *args, **kwargs):
    return auth_views.LogoutView.as_view()(request, *args, **kwargs)

def profile_view(request):
    return HttpResponse("Welcome to your profile page!")
