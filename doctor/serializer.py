from rest_framework import serializers
from .models import Specialization,Designation,AvaliableTime,Reviewer,Doctor


class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = "__all__"


class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = "__all__"



class AvaliableTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvaliableTime
        fields = "__all__"


class ReviewerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviewer
        fields = "__all__"


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"