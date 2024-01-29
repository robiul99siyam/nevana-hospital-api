from django.shortcuts import render
from rest_framework import viewsets
from .models import Specialization,Designation,AvaliableTime,Doctor,Reviewer
from .serializer import SpecializationSerializer,DesignationSerializer,AvaliableTimeSerializer,DoctorSerializer,ReviewerSerializer
from rest_framework import filters

class SpecializationViewset(viewsets.ModelViewSet):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer



class AvaliableTimeViewset(viewsets.ModelViewSet):
    queryset = AvaliableTime.objects.all()
    serializer_class = AvaliableTimeSerializer

class DesignationViewset(viewsets.ModelViewSet):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer


class ReviewerViewset(viewsets.ModelViewSet):
    queryset = Reviewer.objects.all()
    serializer_class = ReviewerSerializer



class DoctorViewset(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__first_name', 'user__email', 'designation__name', 'specialization__name'] 