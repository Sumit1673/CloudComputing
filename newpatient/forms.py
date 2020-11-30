from django import forms
from eyecare_app.models import DataPatinet
# from .models import PatientImage
from random import randrange as rand_num



class PatientAddForm(forms.ModelForm):
    p_ids = DataPatinet.objects.values_list('id')
    new_pid = rand_num(0, 100)
    while new_pid in p_ids:
        new_pid = rand_num(0, 100)

    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    # p_id = str(first_name) +
    patient_id = forms.CharField(max_length=50, required=False, initial=str(new_pid))
    patient_id.disabled = True
    email = forms.EmailField()
    phone = forms.CharField(label='Phone', max_length=12, required=False)
    age = forms.IntegerField(label='Age', required=False)
    image = forms.ImageField(required=True)

    class Meta:
        model = DataPatinet
        fields = ['first_name', 'last_name', 'patient_id','email', 'phone', 'age', 'image',]

# class PatientRetinaImages(forms.Form):
#     class Meta:
#         model = PatientImage
#         fields = ['image']