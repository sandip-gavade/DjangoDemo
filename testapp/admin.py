from django.contrib import admin

from .models import Employee
from .models import Person

admin.site.register(Employee)
admin.site.register(Person)
# Register your models here.
