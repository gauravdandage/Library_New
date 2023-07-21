from django.contrib import admin
from relationship.models import * 
# Register your models here.


admin.site.register([Person, Aadhar, Car, CarModel, FuelType, FourWheeler])