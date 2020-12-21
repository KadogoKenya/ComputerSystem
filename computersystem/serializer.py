from rest_framework import serializers
from .models import Computer

class ComputerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Computer
        fields=['computer','computer_name', 'Operating_system', 'Ip_address','Mac_address','user','location','purchase_date']
