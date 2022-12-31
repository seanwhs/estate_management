from django import forms
from django.forms import ModelForm
from .models import Manager, Property, Unit, Facility, Owner

class ManagerForm(ModelForm):
    class Meta:
        model = Manager
        fields = (
            'company_name', 'family_name', 'given_name', 
            'preferred_name', 'phone', 'email', 'start_date',
        )
        labels = {
            'company_name': '',
            'family_name': '',
            'given_name': '',
            'preferred_name': '',
            'phone': '',
            'email': '',
            'start_date': '',
        }

        widgets = {
            'company_name': forms.TextInput(attrs={'class':'form-conytrol','placeholder':'Company Name'}),
            'family_name': forms.TextInput(attrs={'class':'form-conytrol','placeholder':'Family Name'}),
            'given_name': forms.TextInput(attrs={'class':'form-conytrol','placeholder':'Given Name'}),
            'preferred_name': forms.TextInput(attrs={'class':'form-conytrol','placeholder':'Preferred Name'}),
            'phone': forms.TextInput(attrs={'class':'form-conytrol','placeholder':'Mobile Phone Number'}),
            'email': forms.EmailInput(attrs={'class':'form-conytrol','placeholder':'Email'}),
            'start_date': forms.DateInput(attrs={'class':'form-conytrol','placeholder':'Start Date'}),
        }

class PropertyForm(ModelForm):
    class Meta:
        model = Property
        fields =(
            'name', 'type', 'address', 'postal_code', 'phone', 
            'web', 'email', 'manager', 'contract_period', 'description', 
        )

       
class UnitForm(ModelForm):
    class Meta:
        model = Unit
        fields=(
            'property', 'block', 'floor', 'unit_number', 'owner',
            'share_value', 'ownership_start_date',
        )

class OwnerForm(ModelForm):
    class Meta:
        model = Owner
        fields =(
            'family_name', 'given_name', 'preferred_name', 
            'phone', 'email', 
        )

        labels = {
            'family_name': '',
            'given_name': '',
            'preferred_name': '',
            'phone': '',
            'email': '',
        }

        widgets = {
            'family_name': forms.TextInput(attrs={'class':'form-conytrol','placeholder':'Family Name'}),
            'given_name': forms.TextInput(attrs={'class':'form-conytrol','placeholder':'Given Name'}),
            'preferred_name': forms.TextInput(attrs={'class':'form-conytrol','placeholder':'Preferred Name'}),
            'phone': forms.TextInput(attrs={'class':'form-conytrol','placeholder':'Mobile Phone'}),
            'email': forms.EmailInput(attrs={'class':'form-conytrol','placeholder':'Email'}),
        }


class FacilityForm(ModelForm):
    class Meta:
        model = Facility
        fields = ('name', 'type', 'quantity', 'property', 'description',)

   