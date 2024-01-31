from django.shortcuts import render,redirect
from .models import patient
from rest_framework import viewsets
from .serializer import PatientSerialzer,UserRegister,UserLoingSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.contrib.auth import login,authenticate,logout
from django.utils.encoding import force_bytes
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


#---------------------- email--------------------------------->
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives


#----------------------- patient viewset create now -------------->
class patinetViewset(viewsets.ModelViewSet):
    queryset = patient.objects.all()
    serializer_class = PatientSerialzer






class UserRegistrationApiView(APIView):
    serializer_class = UserRegister
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data) 
        if serializer.is_valid(): 
            user = serializer.save()


            # amar ekane just ekta token make korchi 
            token = default_token_generator.make_token(user)
            print("Token", token)
            # then ekane amar ekta user id create korch
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            print('uid', uid)

            # ar ei khane amar uid end token diye ekta confrim link make korchi 
            confirm_link = f"http://127.0.0.1:8000/patient/active/{uid}/{token}"

            email_subject = "Verify Email in nevana hospital"
            email_body = render_to_string("confrim.html",{'confirm_link' : confirm_link})

            email = EmailMultiAlternatives(email_subject,'',to=[user.email])
            email.attach_alternative(email_body,'text/html')
            email.send()

            print(user)
            return Response("Dear User Check User Email")
        return Response(serializer.errors)

    

def activete(request,uid64,token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid)
    except(user.DoesNotExist):
        user = None
    

    if user is not None and default_token_generator.check_token(user,token):
        user.is_active = True
        user.save()
        return redirect('login')
    else:
        return redirect('register')


class LoginAPIView(APIView):
    def post(self,request):
        serializer = UserLoingSerializer(data= self.request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username=username,password=password)

            if user:
                token,_= Token.objects.get_or_create(user=user)
                print(token)
                print(_)
                login(request,user)
                return Response({'token':token.key,'user_id':user.id})
            else:
                return Response({"errors":"Invalid Data"})
        else:
            return Response(serializer.errors) 


class LogOutApiview(APIView):
    def get(self, request):
        request.user.auth_token.delete()
        logout(request)
        return redirect('login')