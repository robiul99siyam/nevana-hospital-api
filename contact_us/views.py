from django.shortcuts import render
from .models import contact_us
from .serializer import contactSerialzer
from rest_framework import viewsets




#----------------------------- contact us views make now ------------------>

class contactUsViewset(viewsets.ModelViewSet):
    queryset = contact_us.objects.all()
    serializer_class = contactSerialzer
    