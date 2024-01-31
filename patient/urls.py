from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path,include



#-------------- rotuer all -------------------->
routers = DefaultRouter()
routers.register('list',views.patinetViewset)

urlpatterns = [
    path('', include(routers.urls)),
    path('register/',views.UserRegistrationApiView.as_view(),name='register'),
    path('active/<uid64>/<token>/',views.activete,name='activate'),
    path("login/",views.LoginAPIView.as_view(),name='login'),
    path('logout/',views.LogOutApiview.as_view(),name='logout'),
]