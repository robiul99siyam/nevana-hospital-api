from django.contrib import admin
from .models import Appointment
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ["patient_name","doctor_name",'appointment_types',"appointment_status",'time',"symtom","cencle"]

    def patient_name (self,obj):
        return obj.patient.user.first_name

    def doctor_name(self,obj):
        return obj.doctor.user.first_name

    def save_model(self,request,obj,form,change):
        obj.save()
        if obj.appointment_status == 'Running' and obj.appointment_types == 'Online':
            email_subject = "Appointment in nevana hospital"
            email_body = render_to_string("appointment.html",{'user' : obj.patient.user,"doctor":obj.doctor.user,"meet_link":obj.doctor.meet_link})

            email = EmailMultiAlternatives(email_subject,'',to=[obj.patient.user.email])
            email.attach_alternative(email_body,'text/html')
            email.send()

admin.site.register(Appointment,AppointmentAdmin)

# admin.site.register(Appointment)