from django.contrib import admin
from django.urls import path
from . import views
from .forms import ModelForm

urlpatterns = [
    # main master data page
    path('', views.master_data, name='master-data'),
    
    #estate_manager
    path('manager_create/', views.manager_form, name='manager-create'), 
    path('manager_update/<int:id>/', views.manager_form, name='manager-update'),     
    path('manager_list/',views.manager_list, name='manager-list'),
    path('manager_delete/<int:id>/',views.manager_delete, name='manager-delete'),

    #owner
    path('owner_create/', views.owner_form, name='owner-create'), 
    path('owner_update/<int:id>/', views.owner_form, name='owner-update'),     
    path('owner_list/',views.owner_list, name='owner-list'),
    path('owner_delete/<int:id>/',views.owner_delete, name='owner-delete'),
    
    #property
    path('property_create/', views.property_form, name='property-create'), 
    path('property_update/<int:id>/', views.property_form, name='property-update'),     
    path('property_list/',views.property_list, name='property-list'),
    path('property_delete/<int:id>/',views.property_delete, name='property-delete'),

    #units
    path('unit_create/', views.unit_form, name='unit-create'), 
    path('unit_update/<int:id>/', views.unit_form, name='unit-update'),     
    path('unit_list/',views.unit_list, name='unit-list'),
    path('unit_delete/<int:id>/',views.unit_delete, name='unit-delete'),

    #facility
    path('facility_create/', views.facility_form, name='facility-create'), 
    path('facility_update/<int:id>/', views.facility_form, name='facility-update'),     
    path('facility_list/',views.facility_list, name='facility-list'),
    path('facility_delete/<int:id>/',views.facility_delete, name='facility-delete'),
    ]