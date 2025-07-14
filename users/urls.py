from django.urls import path
from . import views

urlpatterns = [
    path('', views.users_home, name='users_home'),  # Option 1: users/ homepage
    # path('', views.redirect_to_login),  # Option 2: redirect users/ to login
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
