from django.shortcuts import render
# from .models import PatientInfo, DiabeticResults
import datetime

def home(request):

    return render(request, 'eyecare_app/home.html')  # returns http response in background


def about(request):
    return render(request, 'eyecare_app/about.html')


# def create_table_on_btn_click(request):
#     add_patient_clicked = request.GET
#     # if add_patient_clicked is not None:
#     return render(request, 'eyecare_app/new_patient.html')


def workspace(request):
    data = [1,2,2,3,4]
    # p_res = DiabeticResults()
    # p_res.result, p_res.ai_score = 3, 93.5
    # p_res.tested_on = datetime.date(2020, 1, 25)
    # p_res.save()
    # p_info = PatientInfo()
    # p_info.result = p_res
    # p_info.first_name = 'Tony'
    # p_info.last_name = 'Stark'
    # p_info.save()
    return render(request, 'eyecare_app/workspace.html', {'btn_clicked': 1, 'data':data})
