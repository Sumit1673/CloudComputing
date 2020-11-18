"""eyecare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from newpatient import views as new_patient_view
from django.conf import settings
from django.conf.urls.static import static
from users import views as view_users


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('newpatient.urls') ),
    # path('register/>', view_users.register, name='register'),
    path('', include('users.urls')),

    path('', include('eyecare_app.urls')),# if you have multiple apps it is
    #  recommended to go with the specific app name. If you have just one then follow the next command
    # path('', include('eyecare_app.urls')),
    # path('', include('patient_profile.urls')),
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

