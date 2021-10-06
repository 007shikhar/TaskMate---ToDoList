from users_app import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', auth_views.LoginView.as_view(template_name='login.html'), name='login'), # if .as_view() is empty, (default) it will search-                                                                             
    path('logout', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),   #-for the template in registration/login.html
]