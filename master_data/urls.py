from django.contrib import admin
from django.urls import path
from . import views
from .forms import ModelForm

urlpatterns = [
    # main master data page
    path('', views.master_data, name='master-data'),
    
    #estate_manager
    path('manager_create/', views.manager_form, name='manager-create'), 
    path('<int:id>/', views.manager_form, name='manager-update'),     
    path('manager_list/',views.manager_list, name='manager-list'),
    path('manager_delete/<int:id>/',views.manager_delete, name='manager-delete'),

    #owner

    #estate_manager

    #property

    #units

    #facility
]
