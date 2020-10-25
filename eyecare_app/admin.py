from django.contrib import admin
from .models import DataDiabetic, DataPatinet
# Register your models here.
admin.site.register(DataPatinet)
admin.site.register(DataDiabetic)
#model has been registered