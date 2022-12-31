from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Manager, Property, Unit, Facility, Owner
from .forms import ManagerForm, PropertyForm, UnitForm, OwnerForm, FacilityForm 


# Master data main page.
def master_data(request):
    context={}
    return render(request, 'master_data/master_data.html', context)

# List data
def property(request):
    property = Property.objects.all()
    context={
        'iterable':property,
        'title': 'Properties',
         }
    return render(request, 'master_data/list_data.html', context)

def facility(request):
    facility = Facility.objects.all()
    context={
        'iterable':facility,
        'title': 'Facilities',
        }
    return render(request, 'master_data/list_data.html', context)

def unit(request):
    unit = Unit.objects.all()
    context={
        'iterable':unit,
        'title': 'Units',

        }
    return render(request, 'master_data/list_data.html', context)

def owner(request):
    owner = Owner.objects.all()
    context={
        'iterable':owner,
        'title': 'Owners',
        }
    return render(request, 'master_data/list_data.html', context)

def estate_manager(request):
    manager = Manager.objects.all()
    context={
        'iterable':manager,
        'title': 'Estate Managers',
        }
    return render(request, 'master_data/list_data.html', context)

# add data
def add_manager(request):
    submitted = False
    if request.method == 'POST':
        form = ManagerForm(request.POST)
        if form.is_valid():
            form.save() # save to DB
            submitted= True
            return redirect('estate-manager')
    else:
        form = ManagerForm()
        if 'submitted' in request.GET:
            submitted = True
        context ={'form':form, 'submitted': submitted, 'title':'Manager'}
        return render(request, 'master_data/add_data.html', context)

def add_property(request):
    submitted = False
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            form.save() # save to DB
            submitted= True
            return redirect('property-data')
    else:
        form = PropertyForm()
        if 'submitted' in request.GET:
            submitted = True
        context ={'form':form, 'submitted': submitted, 'title':'Property'}
        return render(request, 'master_data/add_data.html', context)


def add_unit(request):
    submitted = False
    if request.method == 'POST':
        form = UnitForm(request.POST)
        if form.is_valid():
            form.save() # save to DB
            submitted= True
            return redirect('unit')
    else:
        form = UnitForm()
        if 'submitted' in request.GET:
            submitted = True
        context ={'form':form, 'submitted': submitted, 'title':'Unit'}
        return render(request, 'master_data/add_data.html', context)

def add_owner(request):
    submitted = False
    if request.method == 'POST':
        form = OwnerForm(request.POST)
        if form.is_valid():
            form.save() # save to DB
            submitted= True
            return redirect('owner-data')
    else:
        form = OwnerForm()
        if 'submitted' in request.GET:
            submitted = True
        context ={'form':form, 'submitted': submitted, 'title':'Owner'}
        return render(request, 'master_data/add_data.html', context)


def add_facility(request):
    submitted = False
    if request.method == 'POST':
        form = FacilityForm(request.POST)
        if form.is_valid():
            form.save() # save to DB
            submitted= True
            return redirect('facility')
    else:
        form = FacilityForm()
        if 'submitted' in request.GET:
            submitted = True
        context ={'form':form, 'submitted': submitted, 'title':'Facility'}
        return render(request, 'master_data/add_data.html', context)