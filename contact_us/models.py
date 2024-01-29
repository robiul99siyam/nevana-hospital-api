from django.db import models

#-------------- contact us ------------------->

class contact_us(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    problem = models.TextField()

    class Meta:
        verbose_name_plural = "Contact Us"
