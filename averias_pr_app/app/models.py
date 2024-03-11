from django.db import models
from django import forms

# Create your models here.
class user(models.Model): #Automatically generates id
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  email = models.EmailField(unique=True,null=True)
  password = forms.CharField(widget=forms.PasswordInput)

class report(models.Model):
  date = models.DateTimeField(auto_now_add=True) # Time is saved as soon as the object is created
  email = models.EmailField(unique=True,null=True) # User email that submitted report
  status = models.CharField(max_length=1) # "P" (En proceso) o "R" (Resuelto)

class report_data(models.Model):
  address_line_1 = models.CharField(max_length=255)
  address_line_2 = models.CharField(max_length=255)
  category = models.CharField(max_length=255) # ***Determine the different categories***
  city = models.CharField(max_length=255)
  zipcode = models.CharField(max_length=5)
  geo_data_lat = models.DecimalField(max_digits=5, decimal_places=5)
  geo_data_long = models.DecimalField(max_digits=5, decimal_places=5)
  image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100) # ***Change these arguments later***

class municipality(models.Model):
  name = models.CharField(max_length=255)
  population = models.IntegerField()
  area_size = models.DecimalField(max_digits=5, decimal_places=5)