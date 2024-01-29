from django.db import models
from django.contrib.auth.models import User 

#---------------- patient model create now -------------------->

class patient(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.CharField(max_length=50)
    images = models.ImageField(upload_to='patient/media/images/')

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    
   