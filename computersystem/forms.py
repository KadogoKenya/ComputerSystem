from django import forms
from django.contrib.auth.models import User
from .models import Computer
from users.models import Profile
import cloudinary.uploader
from cloudinary.models import CloudinaryField
import cloudinary




class ComputerForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields=['computer_name', 'Operating_system', 'Ip_address','Mac_address','user','location','purchase_date']

class ComputerSearchForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields=['computer_name','user']