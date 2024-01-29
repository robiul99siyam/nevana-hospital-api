from django.contrib import admin
from .models import Specialization,Designation,Doctor,AvaliableTime,Reviewer



class SpecializationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ['name','slug']
admin.site.register(Specialization,SpecializationAdmin)





class DesignationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ['name','slug']
admin.site.register(Designation,DesignationAdmin)


admin.site.register(Doctor)
admin.site.register(AvaliableTime)
admin.site.register(Reviewer)