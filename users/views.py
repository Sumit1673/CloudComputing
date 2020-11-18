from django.shortcuts import render, redirect
from .forms import UserCreationForm, HospitalForm, LoginForm
from .login_backened import LoginAuthBackened
from django.contrib import messages
from django.contrib.auth import logout, login
from .models import StaffDataModel, HospitalDataModel
from django.forms import modelformset_factory

# Create your views here.
def cus_login(request):
    if request.method =='POST':
        print("I am here1")
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = LoginAuthBackened().authenticate(request=request, username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    messages.success(request, f'Login Successful.')
                    # print('Inside Login View',request.user)
                    # print('Inside Login View', request.user.is_authenticated)
                    return redirect('app-workspace')
                else:
                    print("user inactive")
            else:
                messages.error(request, f'Password Incorrect !')
                return render('app-login')
        else:
            print(form.errors)
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})

def cus_logout(request):
    print('Logging out {}'.format(request.user))
    logout(request)
    messages.success(request, f'Logged Out! Login to continue ...')
    return redirect('app-home')


def register(request):
    if request.method =='POST':
        staff_form = UserCreationForm(request.POST)
        hospital_form = HospitalForm(request.POST)

        if staff_form.is_valid() and hospital_form.is_valid():

            hospital = hospital_form.save()
            staff = staff_form.save(False)
            staff.hospital = hospital
            staff.save()
            messages.success(request, f'Doctor registered successfully. Login Now')
            # redirect to a new URL:
            return redirect('app-login')
        # print(form.errors)

        # form = UserCreationForm()
    else:
        hospital_form = HospitalForm()
        staff_form = UserCreationForm()
    args = {}
    # args.update(csrf(request))
    args['hospital_form'] = hospital_form
    args['staff_form'] = staff_form

    return render(request, 'users/register.html', {'forms':args})

