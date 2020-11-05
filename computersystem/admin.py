from django.contrib import admin
from . models import Computer
from. forms import ComputerForm

# Register your models here.

class ComputerAdmin(admin.ModelAdmin):
    list_display=['computer_name','Ip_address','Mac_address']
    form=ComputerForm
    list_filter=['computer_name','Ip_address']
    search_fields=['computer_name','Ip_address']


admin.site.register(Computer, ComputerAdmin)
