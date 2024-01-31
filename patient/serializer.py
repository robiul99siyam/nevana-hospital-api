from rest_framework import serializers
from .models import patient
from django.contrib.auth.models import User
class PatientSerialzer(serializers.ModelSerializer):
    class Meta:
        model = patient
        fields = '__all__'


class UserRegister(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required = True)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password','confirm_password']


    def save(self):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        password = self.validated_data['password']
        password1 = self.validated_data['confirm_password']


        if password != password1:
            raise serializers.ValidationError({"errors":"Password Don't Match !"})
        
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"errors":"Already Email Exists "})
        
        account = User(username  = username,first_name = first_name,last_name = last_name,email=email)
        print(account)
        account.set_password(password)
        account.is_active = False
        account.save()
        return account


class UserLoingSerializer(serializers.ModelSerializer):
        username = serializers.CharField(required = True)
        password = serializers.CharField(required = True)

        class Meta:
             model = User
             fields = ['username','password']