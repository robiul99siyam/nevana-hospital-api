from django.db import models
from patient.models import patient
from doctor.models import Doctor,AvaliableTime


# Create your models here.


APPOINMENT_STATUS = [
    ('Complated','complated'),
    ('Pending', 'Pending'),
    ('Running', 'Running'),
]

APPOINMENT_TYPES = [
    ('Online','Online'),
    ('Offline','Offline'),
]
class Appointment (models.Model):
    patient = models.ForeignKey(patient,on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    appointment_status = models.CharField(max_length=50,choices=APPOINMENT_STATUS,default='Pending')
    appointment_types = models.CharField(max_length=50,choices=APPOINMENT_TYPES)
    time = models.ForeignKey(AvaliableTime,on_delete=models.CASCADE)
    symtom = models.TextField()
    cencle = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.patient.user.first_name} Doctor : {self.doctor.user.first_name}"