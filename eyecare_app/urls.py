from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'app-home'),
    path('about/', views.about, name= 'app-about')
    path('workspace/', views.about, name= 'app-workspace')
]