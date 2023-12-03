# from django.contrib.admin import views

from . views import *
from django.urls import path, include
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'cus',CustDetailViewSet)
urlpatterns = [
    path('',include(router.urls)),

]