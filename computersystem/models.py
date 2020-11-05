from django.db import models
from django.contrib.auth.models import User
import cloudinary
import cloudinary.uploader
from cloudinary.models import CloudinaryField
from datetime import datetime, date


# Create your models here.

class Computer(models.Model):
    computer_name=models.CharField(max_length=30)
    Ip_address=models.CharField(max_length=20)
    Mac_address=models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    location=models.CharField(max_length=30)
    posted_  date=models.DateTimeField(auto_now=True)
    purchase_date=models.DateField(auto_now_add=False, auto_now=False, blank=True)


    def __str__(self):
        return f'{self.computer_name} Computer'
