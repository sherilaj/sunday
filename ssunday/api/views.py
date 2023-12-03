from django.shortcuts import render
from . models import *
from . serializers import *
from rest_framework import viewsets
# Create your views here.
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustSerializers
class CustDetailViewSet(viewsets.ModelViewSet):
    queryset = CustomerDetails.objects.all()
    serializer_class = CustDetailSerializers


