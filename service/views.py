from django.shortcuts import render
from rest_framework import viewsets
from .models import Service
from .serializer import serviceSerializer

#-------------------- service view set ---------------------->

class serviceViewset(viewsets.ModelViewSet):
    queryset = Service.objects.all() # queryset mane hole amar sokol object gula asbe then serializer class ese ta sob api create kore felbe
    serializer_class = serviceSerializer 

