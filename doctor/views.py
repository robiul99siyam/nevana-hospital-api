from django.shortcuts import render
from rest_framework import viewsets
from .models import Specialization,Designation,AvaliableTime,Doctor,Reviewer
from .serializer import SpecializationSerializer,DesignationSerializer,AvaliableTimeSerializer,DoctorSerializer,ReviewerSerializer
from rest_framework import filters,pagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class SpecializationViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer



class AvaliableTimeViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = AvaliableTime.objects.all()
    serializer_class = AvaliableTimeSerializer

class DesignationViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer


class ReviewerViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Reviewer.objects.all()
    serializer_class = ReviewerSerializer


class DoctorPagination(pagination.PageNumberPagination):
    page_size = 4
    page_size_query_param = page_size
    max_page_size = 100




class DoctorViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    filter_backends = [filters.SearchFilter]
    pagination_class = DoctorPagination
    search_fields = ['user__first_name', 'user__email', 'designation__name', 'speclization__name'] 