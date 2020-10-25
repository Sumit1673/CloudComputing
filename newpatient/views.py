from django.shortcuts import render, redirect
from .forms import  PatientAddForm
from django.contrib import messages

# Create your views here.
def add_new_patient(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        add_form = PatientAddForm(request.POST, request.FILES)
        # image_form = PatientRetinaImages(request.POST)
        # check whether it's valid:
        if add_form.is_valid() :#:and image_form.is_valid():
            # process the data in form.cleaned_data as required
            first_name = add_form.cleaned_data.get('first_name')
            last_name = add_form.cleaned_data.get('last_name')

            add_form.save()

            messages.success(request, f'Patient {first_name} {last_name} created successfully.')
            #redirect to a new URL:
            return redirect('app-workspace')
    else:
        add_form = PatientAddForm()
        # image_form = PatientRetinaImages()

    context =  add_form# 'image_form ':image_form}
    return render(request, 'newpatient/add_new_patient.html', {'form': context})
