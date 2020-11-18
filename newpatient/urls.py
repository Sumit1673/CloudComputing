from django.urls import path
from . import views

urlpatterns = [
    path('addpatient/', views.add_new_patient, name='app-add_new_patient'),

]