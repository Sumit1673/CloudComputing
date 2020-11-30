from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='app-home'),
    path('about/', views.about, name='app-about'),
    path('workspace/', views.workspace, name='app-workspace'),
    path('workspace/1', views.analyze_img, name='app-analyze_retina')

]