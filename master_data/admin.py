from django.contrib import admin
from .models import Manager, Property, Unit, Facility, Owner
# Register your models here.

admin.site.register(Manager)
admin.site.register(Property)
admin.site.register(Unit)
admin.site.register(Facility)
admin.site.register(Owner)