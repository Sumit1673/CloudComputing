from django.db import models

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
    doctor_id = models.IntegerField()
    username = models.CharField(max_length=15, null=True)
    password = models.CharField(max_length=20, null=True)
    # Since a single hospital can have multiple staff that is why one to many
    hospital = models.ForeignKey(HospitalDataModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"Doctor {self.first_name} {self.last_name}"
