from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path,include



#-------------- rotuer all -------------------->
routers = DefaultRouter()
routers.register('specialization', views.SpecializationViewset)
routers.register('designation', views.DesignationViewset)
routers.register('Reviewer', views.ReviewerViewset)
routers.register('List', views.DoctorViewset)
routers.register('Avaliable', views.AvaliableTimeViewset)
urlpatterns = [
    path('', include(routers.urls)),
]