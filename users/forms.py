from django import forms
from random import randrange as rand_num
from .models import HospitalDataModel, StaffDataModel

class UserCreationForm(forms.ModelForm):

    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    username = forms.CharField(label='Username', max_length=100)
    dept_name = forms.CharField(label='Department', max_length=50, required=False)
    doctor_id = forms.IntegerField(initial=str(rand_num(0,100)))
    doctor_id.disabled = True
    # hospital = forms.CharField(label='Hospital', max_length=12, required=False)

    # age = forms.IntegerField(label='Age', required=False)
    # image = forms.ImageField(required=True)
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = StaffDataModel
        fields = [ 'doctor_id', 'first_name', 'last_name', 'username', 'password']

class HospitalForm(forms.ModelForm):
    class Meta:
        model = HospitalDataModel
        fields = '__all__'

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())

