from django.shortcuts import render
from rest_framework import viewsets,pagination
from .models import Service
from .serializer import serviceSerializer


#-------------------- service view set ---------------------->


class servicePagination(pagination.PageNumberPagination):
    page_size=3
    page_size_query_param = page_size
    max_page_size = 100
class serviceViewset(viewsets.ModelViewSet):
    queryset = Service.objects.all() # queryset mane hole amar sokol object gula asbe then serializer class ese ta sob api create kore felbe
    pagination_class = servicePagination
    serializer_class = serviceSerializer 

