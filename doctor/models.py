from django.db import models
from django.contrib.auth.models import User
from patient.models import patient


class Designation(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.name



class Specialization(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.name


class AvaliableTime(models.Model):
    name = models.CharField(max_length=50)

    def  __str__(self):
        return self.name


class Doctor(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    speclization = models.ManyToManyField(Specialization)
    designation = models.ManyToManyField(Designation)
    avaliableTime = models.ManyToManyField(AvaliableTime)
    images = models.ImageField(upload_to='doctor/media/images/')
    fee = models.IntegerField()
    meet_link = models.CharField(max_length=120)


    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


STAR_CHOICES = [
    ('⭐', '⭐'),
    ('⭐⭐', '⭐⭐'),
    ('⭐⭐⭐', '⭐⭐⭐'),
    ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
]

class Reviewer(models.Model):
    reviewer = models.ForeignKey(patient,on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    rating = models.CharField(max_length=40,choices=STAR_CHOICES)

    def __str__(self):
        return f"Patient {self.reviewer.user.first_name} - Doctor {self.doctor.user.first_name}"
