from django.contrib import admin
from .models import HospitalDataModel, StaffDataModel
# Register your models here.
admin.site.register(HospitalDataModel)
admin.site.register(StaffDataModel)