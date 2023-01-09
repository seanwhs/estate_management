from django.shortcuts import render, redirect
from master_data.models import *

# Create your views here.
def billing_main(request):
    context={}
    return render(request, 'billing/billing.html', context)

def billing_list(request):
    search_bill = request.GET.get('search')
    if search_bill:
        list=Unit.objects.filter(
            Q(owner__preferred_name__icontains=search_bill) | #FK
            Q(property__name__icontains=search_bill) | #FK
            Q(block__icontains=search_bill) |
            Q(unit_number__icontains=search_bill)
            )
        # list=Unit.objects.filter(Q(block__icontains=search_bill) | Q(unit_number__icontains=search_bill))

    else:
        # If not searched, return default biling list
        list=Unit.objects.all()


    
    context = {
        'unit_list': list,
        }
    return render(request, "billing/billing_list.html", context)
