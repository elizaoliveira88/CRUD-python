from django.shortcuts import render, redirect
from app.forms import StoresForm
from app.models import Stores


def home(request):
   data = {}
   data['db'] = Stores.objects.all()
   return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = StoresForm
    return render(request, 'form.html', data)

def create(request):
    form = StoresForm(request.POST or None)
    if form.is_valid():
      form.save()
      return redirect('home')
    
def view(request, pk):
    data = {}
    data['db'] = Stores.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Stores.objects.get(pk=pk)
    data['form'] = StoresForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = Stores.objects.get(pk=pk)
    form = StoresForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')
      
def delete(request, pk):
    db = Stores.objects.get(pk=pk)
    db.delete()
    return redirect('home')     
