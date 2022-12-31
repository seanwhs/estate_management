from django.shortcuts import render
from master_data.models import Property

# Create your views here.
def landing(request):
    property = Property.objects.all()
    context={'property':property,}
    return render(request, 'main/landing.html', context)