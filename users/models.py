from django.db import models
from django.utils import timezone
from datetime import datetime

# Create your models here.
# One Hospital can have multiple staffs. So many to one/one to many
class HospitalDataModel(models.Model):
    '''
    for many to one (one to many) the model which is used as foreign key has to be saved
    use ".save()" method before it is added to its relationship model.
    For example: HospitalDataModel is to be saved before it is used in StaffDataModel
    There is no primary key for now.
    '''
    hospital_name = models.CharField(max_length=50)

    def __str__(self):
        return f"Hospital Added: {self.hospital_name}"


class StaffDataModel(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dept_name = models.CharField(max_length=50)
    doctor_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=15, null=False)
    password = models.CharField(max_length=20, null=True)
    last_login = models.DateTimeField(default=timezone.now) # for login purpose
    hospital = models.ForeignKey(HospitalDataModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"Doctor {self.first_name} {self.last_name}"

    def is_authenticated(self):
        return True