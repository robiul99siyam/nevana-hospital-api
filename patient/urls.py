from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path,include



#-------------- rotuer all -------------------->
routers = DefaultRouter()
routers.register('list',views.patinetViewset)

urlpatterns = [
    path('', include(routers.urls)),
]