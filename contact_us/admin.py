from django.contrib import admin
from .models import contact_us


#--------------- contact us register ----------------------------->
class contactAdmin(admin.ModelAdmin):
    list_display = ['name','phone','problem']
admin.site.register(contact_us,contactAdmin)
