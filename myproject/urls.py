"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from attendance.views import attendance_home
from users import urls as user_urls  # Import your custom user management app
from users.views import profile_view

urlpatterns = [
    path('users/', include(user_urls)),  # Custom user management app
    path('admin/', admin.site.urls),
    path('attendance/', include('attendance.urls')),
    path('accounts/profile/', profile_view, name='profile'),
    path('', attendance_home),  # homepage view
]
