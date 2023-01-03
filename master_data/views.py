from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
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
            messages.success(request, ('Manager has been saved successfuly!'))
        else:
            messages.success(request, (str(form.errors)))
        return redirect('manager-list')

def manager_delete(request, id):
    manager = Manager.objects.get(pk=id)
    manager.delete()
    messages.success(request, ('Manager has been deleted!'))
    return redirect('manager-list')

#owner
def owner_list(request):
    context = {'owner_list': Owner.objects.all()}
    return render(request, "master_data/owner_list.html", context)

def owner_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = OwnerForm()
        else:
            owner = Owner.objects.get(pk=id)
            form = OwnerForm(instance=owner)
        return render(request, "master_data/owner_form.html", {'form': form})
    else:
        if id == 0:
            form = OwnerForm(request.POST)
        else:
            owner = Owner.objects.get(pk=id)
            form = OwnerForm(request.POST,instance= owner)
        if form.is_valid():
            form.save()
            messages.success(request, ('Owner has been saved successfuly!'))
        else:
            messages.success(request, (str(form.errors)))
        return redirect('owner-list')

def owner_delete(request, id):
    owner = Owner.objects.get(pk=id)
    owner.delete()
    messages.success(request, ('Owner has been deleted!'))
    return redirect('owner-list')

#property
def property_list(request):
    context = {'property_list': Property.objects.all()}
    return render(request, "master_data/property_list.html", context)

def property_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = PropertyForm()
        else:
            property = Property.objects.get(pk=id)
            form = PropertyForm(instance=property)
        return render(request, "master_data/property_form.html", {'form': form})
    else:
        if id == 0:
            form = PropertyForm(request.POST)
        else:
            property = Property.objects.get(pk=id)
            form = PropertyForm(request.POST,instance= property)
        if form.is_valid():
            form.save()
            messages.success(request, ('Property has been saved successfuly!'))
        else:
            messages.success(request, (str(form.errors)))
        return redirect('property-list')

def property_delete(request, id):
    property = Property.objects.get(pk=id)
    property.delete()
    messages.success(request, ('Property has been deleted!'))
    return redirect('property-list')

#units
def unit_list(request):
    context = {'unit_list': Unit.objects.all()}
    return render(request, "master_data/unit_list.html", context)

def unit_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = UnitForm()
        else:
            unit = Unit.objects.get(pk=id)
            form = UnitForm(instance=unit)
        return render(request, "master_data/unit_form.html", {'form': form})
    else:
        if id == 0:
            form = UnitForm(request.POST)
        else:
            unit = Unit.objects.get(pk=id)
            form = UnitForm(request.POST,instance= unit)
        if form.is_valid():
            form.save()
            messages.success(request, ('Unit has been saved successfuly!'))
        else:
            messages.success(request, (str(form.errors)))
        return redirect('unit-list')

def unit_delete(request, id):
    property = Unit.objects.get(pk=id)
    property.delete()
    messages.success(request, ('Unit has been deleted!'))
    return redirect('unit-list')

#facility
def facility_list(request):
    context = {'facility_list': Facility.objects.all()}
    return render(request, "master_data/facility_list.html", context)

def facility_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = FacilityForm()
        else:
            facility = Facility.objects.get(pk=id)
            form = FacilityForm(instance=facility)
        return render(request, "master_data/facility_form.html", {'form': form})
    else:
        if id == 0:
            form = FacilityForm(request.POST)
        else:
            facility = Facility.objects.get(pk=id)
            form = FacilityForm(request.POST,instance= facility)
        if form.is_valid():
            form.save()
            messages.success(request, ('Facility has been saved successfuly!'))
        else:
            messages.success(request, (str(form.errors)))
        return redirect('facility-list')

def facility_delete(request, id):
    property = Facility.objects.get(pk=id)
    property.delete()
    messages.success(request, ('Facility has been deleted!'))
    return redirect('facility-list')