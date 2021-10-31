from django.contrib import admin

# Register your models here.
from Employees.models import Person

admin.site.register(Person)