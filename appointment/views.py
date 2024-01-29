from django.shortcuts import render
from .models import Appointment
from .serializer import AppointmentSerializer
from rest_framework import viewsets
# Create your views here.


class AppointmentViewset(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    # ei function er mane hole je get queryset kore amora all patient fileter korlam 
    def get_queryset(self):
        queryset = super().get_queryset() # 9 number line er patient ke inhertance korlam
        patient_id = self.request.query_params.get('patient_id')
        if patient_id:
            queryset = queryset.filter(patient_id=patient_id)
        return queryset