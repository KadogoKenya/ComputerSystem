from django.shortcuts import render,redirect
from .forms import ComputerForm,ComputerSearchForm,OperatingsystemForm
from .models import Computer,Operatingsystem
from django.shortcuts import get_object_or_404
from django.contrib import messages

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ComputerSerializer
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='/login/')
def index(request):
    return render(request, 'computer/index.html')


@login_required(login_url='/login/')
def computers(request):
    
    computers=Computer.objects.all()
    computers=computers[::-1]

    form = ComputerSearchForm(request.POST or None)
    context={
        'computers':computers,
        'form':form
    }
    if request.method == 'POST':
        computers=Computer.objects.all().order_by('posted_date').filter(computer_name_incontains=form['computer_name'].value())


        context={
            'computers':computers,
            'form':form
        }

    return render(request,'computer/computers.html',context)


@login_required(login_url='/login/')
def computer_entry(request):
    title='Add computer'
    form = ComputerForm(request.POST or None)
    current_user = request.user
    profile = request.user.profile

    if request.method == 'POST':
        
        form = ComputerForm(request.POST, request.FILES)
        if form.is_valid():
            computer = form.save(commit=False)
            computer.Admin = current_user
            computer.admin_profile = profile
            computer.save()

            messages.success(request,'Successfully saved')
        return redirect('computers')

    else:
        
        form = ComputerForm()

    return render(request,'computer/computer_entry.html',{"form":form})


@login_required(login_url='/login/')
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

@login_required(login_url='/login/')
def computer_edit(request, id=None):
    instance=get_object_or_404(Computer, id=id)
    form = ComputerForm(request.POST or None ,instance = instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

        messages.success(request,'Successfully saved')

        return redirect ('computers')

    context = {
        'instance':instance,
        'form':form
    }

    return render(request,'computer/computer_entry.html', context)


@login_required(login_url='/login/')
def computer_delete(request, id=None):
    instance=get_object_or_404(Computer, id=id)
    # form = ComputerForm(request.POST or None ,instance = instance)
    # if form.is_valid():
    #     instance = form.save(commit=False)
    instance.delete()
    return redirect ('computers')


@login_required(login_url='/login/')
def operating_system(request):
    title='Add Operating system'
    # form = ComputerForm(request.POST or None)
    current_user = request.user
    profile = request.user.profile

    if request.method == 'POST':
        
        form = OperatingsystemForm(request.POST, request.FILES)
        if form.is_valid():
            system = form.save(commit=False)
            system.Admin = current_user
            system.admin_profile = profile
            system.save()

            messages.success(request,'Successfully saved')
        return redirect('computers')

    else:
        
        form = OperatingsystemForm()

    return render(request,'computer/operating_system.html',{"form":form})


class ComputerList(APIView):
    def get(self, request, format=None):
        all_merch = Computer.objects.all()
        serializers = ComputerSerializer(all_merch, many=True)
        return Response(serializers.data)