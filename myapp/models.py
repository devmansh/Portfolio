from pyexpat import model
from typing_extensions import Required
from django.db import models

# Create your models here.
class Services(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=500)
    
    
class AboutMe(models.Model):
    bio = models.TextField()
    dob = models.CharField(max_length=25)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=255)
    address = models.CharField(max_length=50)
    
class Contact(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    def __str__(self):
        return self.name
    