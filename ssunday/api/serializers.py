from . models import *
from rest_framework import serializers

class CustSerializers(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields=('cid','first_name','last_name')
class CustDetailSerializers(serializers.ModelSerializer):
    forkey=CustSerializers()
    class Meta:
        model=CustomerDetails
        fields=('cd_id','c_type','forkey')

