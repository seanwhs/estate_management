from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Manager, Property, Unit, Facility, Owner
from .forms import ManagerForm, PropertyForm, UnitForm, OwnerForm, FacilityForm 


# Master data main page.
def master_data(request):
    context={}
    return render(request, 'master_data/master_data.html', context)

#estate_manager
def manager_list(request):
    context = {'manager_list': Manager.objects.all()}
    return render(request, "master_data/manager_list.html", context)

def manager_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = ManagerForm()
        else:
            manager = Manager.objects.get(pk=id)
            form = ManagerForm(instance=manager)
        return render(request, "master_data/manager_form.html", {'form': form})
    else:
        if id == 0:
            form = ManagerForm(request.POST)
        else:
            manager = Manager.objects.get(pk=id)
            form = ManagerForm(request.POST,instance= manager)
        if form.is_valid():
            form.save()
        return redirect('/master_data/manager_list')

def manager_delete(request, id):
    manager = Manager.objects.get(pk=id)
    manager.delete()
    return redirect('/master_data/manager_list')

#owner

#estate_manager

#property

#units

#facility