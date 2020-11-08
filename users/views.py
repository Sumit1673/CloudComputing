from django.shortcuts import render, redirect
from .forms import UserCreationForm, HospitalForm
from django.contrib import messages
from .models import StaffDataModel, HospitalDataModel
from django.forms import modelformset_factory

# Create your views here.
def register(request):
    if request.method =='POST':
        staff_form = UserCreationForm(request.POST)
        hospital_form = HospitalForm(request.POST)

        if staff_form.is_valid() and hospital_form.is_valid():
            hospital = hospital_form.save()
            staff = staff_form.save(False)
            staff.hospital = hospital
            staff.save()
            messages.success(request, f'Doctor registered successfully.')
            # redirect to a new URL:
            return redirect('app-workspace')
        # print(form.errors)

        # form = UserCreationForm()
    else:
        hospital_form = HospitalForm()
        staff_form = UserCreationForm()
    args = {}
    # args.update(csrf(request))
    args['hospital_form'] = hospital_form
    args['staff_form'] = staff_form
    return render(request, 'users/register.html', args)

