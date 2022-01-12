from django.db import models
from django.db.models.aggregates import Count
from django.db.models.base import Model

# Create your models here.
class user(models.Model):
    email=models.CharField(max_length=100,unique=True)
    password=models.CharField(max_length=100)
    role=models.CharField(max_length=100)
class Developer(models.Model):
    user_id=models.ForeignKey(user,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    dob=models.CharField(max_length=10,null=True)
    gender=models.CharField(max_length=10,null=True)
    address=models.CharField(max_length=100,null=True)
    country=models.CharField(max_length=100,null=True)
    state=models.CharField(max_length=100,null=True)
    phone_number=models.CharField(max_length=10, null=True)
    pincode=models.CharField(max_length=10,null=True)
class Tester(models.Model):
    user_id=models.ForeignKey(user,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    dob=models.CharField(max_length=10,null=True)
    gender=models.CharField(max_length=10,null=True)
    address=models.CharField(max_length=100,null=True)
    country=models.CharField(max_length=100,null=True)
    state=models.CharField(max_length=100,null=True)
    phone_number=models.CharField(max_length=10,null=True)
    pincode=models.CharField(max_length=10,null=True)
class HR(models.Model):
    user_id=models.ForeignKey(user,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    dob=models.CharField(max_length=10,null=True)
    gender=models.CharField(max_length=10,null=True)
    address=models.CharField(max_length=100,null=True)
    country=models.CharField(max_length=100,null=True)
    state=models.CharField(max_length=100,null=True)
    phone_number=models.CharField(max_length=10,null=True)
    pincode=models.CharField(max_length=10,null=True)

class Manager(models.Model):
    user_id=models.ForeignKey(user,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    dob=models.CharField(max_length=10,null=True)
    gender=models.CharField(max_length=10,null=True)
    address=models.CharField(max_length=100,null=True)
    country=models.CharField(max_length=100,null=True)
    state=models.CharField(max_length=100,null=True)
    phone_number=models.CharField(max_length=10,null=True)
    pincode=models.CharField(max_length=10,null=True)
