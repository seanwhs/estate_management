from django.db import models
from django.db.models.functions import Now
from django.db.models import Q 

class Manager(models.Model):   
    company_name = models.CharField(max_length=250)
    family_name = models.CharField(max_length=250)
    given_name = models.CharField(max_length=250)
    preferred_name = models.CharField(max_length=250)
    phone = models.CharField(max_length=10)
    email=models.EmailField(
        unique=True, 
        error_messages={
            'unique':'Thie email has already ben registered'
        }
        )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['given_name', 'family_name'], name='unique_manager'),
        ]
        

    def __str__(self):
        return self.preferred_name


class Property(models.Model):
    PROPERTY_TYPE = [
        ('L', 'Leasehold'),
        ('F', 'Freehold'),
        ('O', 'Others'),
    ]

    CONTRACT_PERIOD =[
        ('1', '1 Year'),
        ('3', '3 Years'),
        ('5', '5 Years'),
    ]
    name = models.CharField(max_length=250)
    type = models.CharField(max_length=1, choices=PROPERTY_TYPE)
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=10)
    phone = models.CharField(max_length=10)
    web = models.URLField()
    email=models.EmailField(
        unique=True, 
        error_messages={
            'unique':'Thie email has already ben registered'
        }
        )
    manager= models.ForeignKey('Manager', null=True, on_delete=models.SET_NULL)
    contract_period=models.CharField(max_length=1, choices=CONTRACT_PERIOD)
    start_date=models.DateField()
    description=models.TextField(null=True, blank=True)

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=Q(start_date__lte=Now()),
                name = "start_date must be less than or equal today"
            )
    ]
  
    def __str__(self):
        return self.name

class Facility(models.Model):
    property=models.ForeignKey(Property, on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    type=models.CharField(max_length=50)
    description=models.TextField()

    def __str__(self):
        return str(self.property) + ', Facility: ' + str(self.name)
       
class Owner(models.Model):
    family_name = models.CharField(max_length=250)
    given_name = models.CharField(max_length=250)
    preferred_name = models.CharField(max_length=250)
    phone = models.CharField(max_length=10)
    email=models.EmailField(
        unique=True, 
        error_messages={
            'unique':'Thie email has already ben registered'
        }
        )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['given_name', 'family_name'], name='unique_owner'),
        ]

    def __str__(self):
        return self.preferred_name

class Unit(models.Model):
    property=models.ForeignKey(Property, on_delete=models.CASCADE)
    block=models.CharField(max_length=50, null=True, blank=True)
    floor=models.CharField(max_length=50, null=True, blank=True)
    unit_number=models.CharField(max_length=10)   
    owner = models.ForeignKey(Owner, null=True, blank=True, on_delete=models.SET_NULL)
    share_value = models.PositiveIntegerField(null=True, blank=True, default=100)
    ownership_start_date=models.DateField()
    
    class Meta:
        constraints = [
            models.CheckConstraint(
                check=Q(ownership_start_date__lte=Now()),
                name = "ownership_start_date must be less than or equal today"
            )
    ]

    def __str__(self):
        string = str(self.property) + ', Blk: ' + str(self.block) + ', Flr: ' + str(self.floor) + ', Unit: ' + str(self.unit_number)
        return string

class Facility(models.Model):
    FACILITY_TYPE = [
        ('SP', 'Swimming Pool'),
        ('PG', 'Childrens Playground'),
        ('BP', 'BBQ Pit'),
        ('L', ' Music Lounge'),
        ('CS', 'Convenience Store'),
        ('MR', ' Meeting Room'),
        ('O', 'Others'),
    ]
    name=models.CharField(max_length=50)
    type = models.CharField(max_length=5, choices=FACILITY_TYPE)
    quantity = models.PositiveIntegerField(default=1)
    property = models.ForeignKey(Property, null=True, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['property', 'name'], name='unique_facility'),
        ]

    def __str__(self):
        return  str(self.property) + ', Facility: ' + str(self.name) + ', ' + str(self.type)

