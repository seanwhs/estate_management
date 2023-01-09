from django.shortcuts import render, redirect
from master_data.models import *

# Create your views here.
def billing_main(request):
    context={}
    return render(request, 'billing/billing.html', context)

def billing_list(request):
    list=Unit.objects.all()
    
    context = {
        'unit_list': Unit.objects.all(),
        }
    return render(request, "billing/billing_list.html", context)
