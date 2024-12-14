from django.shortcuts import render,redirect
from .models import Crud
from .forms import Crudform
from django.contrib import messages

# Create your views here.


def index(request):
    if request.method == 'POST':
        co = Crudform(request.POST)
        if co.is_valid():
            co.save()
            messages.success(request, 'Record Added Successfully')
        return redirect('index')
    else:
        co = Crudform()
        cp = Crud.objects.all()
    return render(request,'core/index.html',{'co' : co, 'cp' : cp})

def delete(request,id):
    if request.method == 'POST':
        cp = Crud.objects.get(pk=id)
        cp.delete()
        return redirect('index')
    
def update(request,id):
    if request.method == 'POST':
        cp = Crud.objects.get(pk=id)
        co = Crudform(request.POST, instance=cp)
        if co.is_valid():
            co.save()
            messages.success(request, 'Record Updated Successfully')
    else:
        cp = Crud.objects.get(pk=id)
        co = Crudform(instance=cp)
    return render(request,'core/update.html', {'co': co})