from django.shortcuts import render,redirect
from .forms import ComputerForm
from .models import Computer


# Create your views here.


def index(request):
    return render(request, 'computer/index.html')

def computers(request):
    computers=Computer.objects.all()
    computers=computers[::-1]

    context={
        'computers':computers
    }

    return render(request,'computer/computers.html',context)



