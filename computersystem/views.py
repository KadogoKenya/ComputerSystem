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
    title='Add computer'
    # form = ComputerForm(request.POST or None)
    current_user = request.user
    profile = request.user.profile

    if request.method == 'POST':
        form = ComputerForm(request.POST, request.FILES)
        if form.is_valid():
            computer = form.save(commit=False)
            computer.Admin = current_user
            computer.admin_profile = profile
            computer.save()
        return redirect('computers')

    else:
        
        form = ComputerForm()

    return render(request,'computer/computer_entry.html',{"form":form})

def computer_list(request):
    title='List of all computers'
    # form = ComputerForm(request.POST or None)
    current_user = request.user
    profile = request.user.profile

    computers=Computer.objects.all()
    context = {
        'computers':computers
    }


    return render(request,'computer/computer_list.html',context)
