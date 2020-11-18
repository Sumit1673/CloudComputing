from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register, name='app-register'),
    path('login/', views.cus_login, name='app-login'),
    path('logout/', views.cus_logout, name='app-logout'),
]