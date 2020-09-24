from django.shortcuts import render 

# Create your views here.
def home(request):
    return render(request, 'eyecare_app/home.html') # returns httpresponse in background


def about(request):
    return render(request, 'eyecare_app/about.html') 

def workspace(request):
    return render(request, 'eyecare_app/workspace.html')
