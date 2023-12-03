from django.db import models

# Create your models here.
class Customer(models.Model):
    cid = models.BigAutoField(primary_key=True)
    first_name=models.CharField(max_length=24)
    last_name = models.CharField(max_length=24)
    def __str__(self):
        return self.first_name
class CustomerDetails(models.Model):
    cd_id = models.BigAutoField(primary_key=True)
    c_type=models.CharField(max_length=24)
    forkey = models.ForeignKey(Customer,on_delete=models.CASCADE)
    def __str__(self):
        return self.c_type