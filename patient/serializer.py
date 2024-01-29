from rest_framework import serializers
from .models import patient
from django.contrib.auth.models import User
class PatientSerialzer(serializers.ModelSerializer):
    class Meta:
        model = patient
        fields = '__all__'


