from django.db import models

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    images = models.ImageField(upload_to='service/media/images')


    def __str__(self):
        return f"service name : {self.name} "
    