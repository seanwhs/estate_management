from django.contrib import admin
from django.urls import path
from . import views
from .forms import ModelForm

urlpatterns = [
    path('', views.master_data, name='master-data'),
    path('property/', views.property, name="property-data"),
    path('owner/', views.owner, name="owner-data"),
    path('manager/', views.estate_manager, name='estate-manager'),
    path('unit/', views.unit, name='unit'),
    path('facility/', views.facility, name='facility'),


    path('add_manager/', views.add_manager, name='add-manager'),
    path('add_property/', views.add_property, name='add-property'),
    path('add_unit/', views.add_unit, name='add-unit'),
    path('add_owner/', views.add_owner, name='add-owner'),
    path('add_facility/', views.add_facility, name='add-facility'),


]
