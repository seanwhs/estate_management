from django.shortcuts import render, redirect
from master_data.models import *

from django.http import HttpResponse, HttpRequest
from django.views import View  
from django.views.generic import View

from .utils import *
import datetime
import pdfkit
import os
from django.contrib import messages


from django.core.mail import EmailMessage, get_connection
from django.template.loader import render_to_string 
from django.conf import settings

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
        request.session['search_bill'] = search_bill
        # list=Unit.objects.filter(Q(block__icontains=search_bill) | Q(unit_number__icontains=search_bill))
    elif not search_bill or search_bill == '':
        request.session['search_bill'] = ''
        # If not searched, return default biling list
        list=Unit.objects.all()

    maint_total = 0
    sink_total=0
    for unit in list:
        maint_payable = (unit.maintenance_fee_monthly * unit.share_value)/100
        sink_payable = (unit.sinking_fund_monthly * unit.share_value)/100
        maint_total += maint_payable
        sink_total += sink_payable

    context = {
        'unit_list': list,
        'maint_total': maint_total,
        'sink_total': sink_total,
            }

    
    return render(request, "billing/billing_list.html", context)


class GeneratePdf(View):
    def get(self, request, *args, **kwargs):   

        search_bill= request.session['search_bill'] 

        if search_bill:
            list=Unit.objects.filter(
                Q(owner__preferred_name__icontains=search_bill) | #FK
                Q(property__name__icontains=search_bill) | #FK
                Q(block__icontains=search_bill) |
                Q(unit_number__icontains=search_bill)
                )
           
            # list=Unit.objects.filter(Q(block__icontains=search_bill) | Q(unit_number__icontains=search_bill))
        elif not search_bill or search_bill =='':
            # If not searched, return default biling list
            list=Unit.objects.all()
               
       
        maint_total = 0
        sink_total=0
        for unit in list:
            maint_payable = (unit.maintenance_fee_monthly * unit.share_value)/100
            sink_payable = (unit.sinking_fund_monthly * unit.share_value)/100
            maint_total += maint_payable
            sink_total += sink_payable

        context = {
            'today': datetime.date.today(), 
            'list': list,
            'maint_total': maint_total,
            'sink_total': sink_total,
                }

        pdf = render_to_pdf('billing/pdf_list.html', context)
        return HttpResponse(pdf, content_type='application/pdf')


def send_email(request):

    search_bill= request.session['search_bill'] 

    if search_bill:
        list=Unit.objects.filter(
            Q(owner__preferred_name__icontains=search_bill) | #FK
            Q(property__name__icontains=search_bill) | #FK
            Q(block__icontains=search_bill) |
            Q(unit_number__icontains=search_bill)
            )
           
        # list=Unit.objects.filter(Q(block__icontains=search_bill) | Q(unit_number__icontains=search_bill))
    elif not search_bill or search_bill =='':
        # If not searched, return default biling list
        list=Unit.objects.all()
            
    maint_total = 0
    sink_total=0
    for unit in list:
        maint_payable = (unit.maintenance_fee_monthly * unit.share_value)/100
        sink_payable = (unit.sinking_fund_monthly * unit.share_value)/100
        maint_total += maint_payable
        sink_total += sink_payable

    context = {
        'today': datetime.date.today(), 
        'list': list,
        'maint_total': maint_total,
        'sink_total': sink_total,
            }
    

    #HTML FIle to be converted to PDF - inside your Django directory
    template = get_template('billing/pdf_list.html')


    #Render the HTML
    html = template.render(context)

    #Options - Very Important [Don't forget this]
    options = {
          'encoding': 'UTF-8',
          'javascript-delay':'1000', #Optional
          'enable-local-file-access': None, #To be able to access CSS
          'page-size': 'A4',
          'custom-header' : [
              ('Accept-Encoding', 'gzip')
          ],
      }
      #Javascript delay is optional

    #Remember that location to wkhtmltopdf
    path_wkthmltopdf = 'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)

    #Saving the File
    filepath = os.path.join(settings.MEDIA_ROOT, 'sample_billing')
    os.makedirs(filepath, exist_ok=True)
    pdf_save_path = filepath+'sample_bill.pdf'
    #Save the PDF
    pdfkit.from_string(html, pdf_save_path, configuration=config, options=options)


    #send the emails to client
    to_email = 'seanwhs@hotmail.com'
    from_client = 'seanwhs@hotmail.com'
    email_bill(to_email, from_client, pdf_save_path)
    messages.success(request, "Email sent succesfully")



    #Email was send, redirect back to view - invoice
    # messages.success(request, "Email sent to the client succesfully")
    return redirect('billing-list')

    
    