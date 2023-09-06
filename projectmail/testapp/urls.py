from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views

from testapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sendmail/', views.sendmail, name='sendmail'),
    path('data/', views.datalist, name='data'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='testapp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='testapp/logout.html'), name='logout'),


]