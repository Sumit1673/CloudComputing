from django.shortcuts import render
# from .models import PatientInfo, DiabeticResults
from django.contrib.auth.decorators import login_required
from users.views import login

def home(request):

    return render(request, 'eyecare_app/home.html')  # returns http response in background


def about(request):
    return render(request, 'eyecare_app/about.html')


# def create_table_on_btn_click(request):
#     add_patient_clicked = request.GET
#     # if add_patient_clicked is not None:
#     return render(request, 'eyecare_app/new_patient.html')

@login_required
def workspace(request):
    data = [1,2,2,3,4]
    return render(request, 'eyecare_app/workspace.html', {'btn_clicked': 1, 'data':data})
