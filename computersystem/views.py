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

def computer_entry(request):
    title=Add computer
    # form = ComputerForm(request.POST or None)
    if request.method == 'POST':
        form = ComputerForm(request.POST)
        if form.is_valid():
            context={
                'title':title,
                'form':form,
            }

    return render(request,'computer/computer_entry.html',context)
