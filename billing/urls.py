from django.contrib import admin
from django.urls import path
from . import views
from .views import GeneratePdf
# from .forms import ModelForm

urlpatterns = [
    # main master data page
    path('', views.billing_main, name='billing-main'),
    path('list/', views.billing_list, name='billing-list'),
    path('pdf/', GeneratePdf.as_view(), name='pdf-list'),
   
    ]