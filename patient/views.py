from django.shortcuts import render,redirect
from .models import patient
from rest_framework import viewsets
from .serializer import PatientSerialzer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.contrib.auth import login,authenticate,logout
from django.utils.encoding import force_bytes



#---------------------- email--------------------------------->
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives


#----------------------- patient viewset create now -------------->
class patinetViewset(viewsets.ModelViewSet):
    queryset = patient.objects.all()
    serializer_class = PatientSerialzer



# class UserRegistrationApiView(APIView):
#     serializer_class = RegistrationSerializer
    
#     def post(self, request):
#         serializer = self.serializer_class(data=request.data) 
#         if serializer.is_valid(): 
#             user = serializer.save()


#             # amar ekane just ekta token make korchi 
#             token = default_token_generator.make_token(user)
#             print("Token", token)
#             # then ekane amar ekta user id create korch
#             uid = urlsafe_base64_encode(force_bytes(user.pk))
#             print('uid', uid)

#             # ar ei khane amar uid end token diye ekta confrim link make korchi 
#             confrim_link = f"http://127.0.0.1:8000/patient/active/{uid}/{token}"

#             print(user)
#             return Response("Done")
#         return Response(serializer.errors)