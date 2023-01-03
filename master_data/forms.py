from django import forms
from django.forms import ModelForm
from .models import Manager, Property, Unit, Facility, Owner

class DateInput(forms.DateInput):
    input_type = 'date'

class ManagerForm(ModelForm):
    class Meta:
        model = Manager
        fields = (
            'company_name', 'family_name', 'given_name', 
            'preferred_name', 'phone', 'email', 
        )
        labels = {
            'company_name': 'Company Name',
            'family_name': 'Family Name',
            'given_name': 'Given Name',
            'preferred_name': 'Preferred Name',
            'phone': 'Phone',
            'email': 'Email',
        }

        widgets = {
            'company_name': forms.TextInput(attrs={'class':'form-conytrol','placeholder':'Company Name'}),
            'family_name': forms.TextInput(attrs={'class':'form-conytrol','placeholder':'Family Name'}),
            'given_name': forms.TextInput(attrs={'class':'form-conytrol','placeholder':'Given Name'}),
            'preferred_name': forms.TextInput(attrs={'class':'form-conytrol','placeholder':'Preferred Name'}),
            'phone': forms.TextInput(attrs={'class':'form-conytrol','placeholder':'Mobile Phone Number'}),
            'email': forms.EmailInput(attrs={'class':'form-conytrol','placeholder':'Email'}),
        }

class PropertyForm(ModelForm):
    class Meta:
        model = Property
        fields =(
            'name', 'type', 'address', 'postal_code', 'phone', 
            'web', 'email', 'manager', 'contract_period', 'start_date', 'description', 
        )
        widgets = {
            'start_date': DateInput(),
        }


class UnitForm(ModelForm):
    class Meta:
        model = Unit
        fields=(
            'property', 'block', 'floor', 'unit_number', 'owner',
            'share_value', 'ownership_start_date',
        )
        widgets = {
            'ownership_start_date': DateInput(),
        }

class OwnerForm(ModelForm):
    class Meta:
        model = Owner
        fields =(
            'family_name', 'given_name', 'preferred_name', 
            'phone', 'email', 
        )

        labels = {
            'family_name': 'Family Name',
            'given_name': 'Given Name',
            'preferred_name': 'Preferred Name',
            'phone': 'Phone',
            'email': 'Email',
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

   