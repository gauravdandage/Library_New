

# exec(open(r"C:\Users\Administrator\Desktop\DjangoProjects\sample_library\relationship\db_shell.py").read())

from relationship.models import *

# Person.objects.create(name="CBA", age=24, mobile=7854786585, email="cba@gmail.com")

# all = Person.objects.all()
# print(list(all))


# a1 = Person.objects.get(id=3)
# print(a1)

from django.utils import timezone 
from datetime import date
import time


# create new aadhar data
#  
# first way 
# Aadhar.objects.create(aadhar_number=458455655822, address="Jalna", DOB=date(1987, 7, 21), person=a1)

# second way 
# Aadhar.objects.create(aadhar_number=875455655822, address="Beed", DOB=date(1991, 11, 24), person_id=2)

# Aadhar.objects.create(aadhar_number=775455655822, address="Dhule", DOB=date(1998, 2, 6), person_id=3)


# p1 = Aadhar.objects.get(aadhar_number=875455655822)
# print(p1)
# print(p1.person)


# aadhar se person nikala/ fetch
# p2 = Aadhar.objects.get(id=3)                  # CBA
# print(p2.person.age)


# person se aadhar fetch

# p4 = Person.objects.get(id=3)
# print(p4.aadhar.address)
# print(p4.aadhar.__dict__)


# for i in Aadhar.objects.all():
#     print(i.person)         # get all person name


# c1 = time.time()
# for i in Aadhar.objects.all():
#     print(i)            # get all adhar num
# c2 = time.time()
# print(c2 - c1)


# ---------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------


# code optimization -- to reduce time 

# for i in Aadhar.objects.all().select_related("person"):
#     print(i)        # get all addhar nub


# b1 = time.time()
# for i in Aadhar.objects.all().select_related("person"):
#     print(i.person)       # get all person name
# b2 = time.time()
# print(b2 - b1)


# for y in Person.objects.all():
#     print(y.aadhar)

# -----------------------------------------------------------------------------------------------------


from relationship.models import Car, CarModel

# honda = Car.objects.create(name="Honda")
# mahindra = Car.objects.create(name="Mahindra")

# data = Car.objects.all()
# print(data)


# create car model 
# mahindra = Car.objects.get(name='Mahindra')
# thar = CarModel.objects.create(name="Thar", car=mahindra)
# scorpio = CarModel.objects.create(name="Scorpio-N", car=mahindra)
# XUV700 = CarModel.objects.create(name="XUV700", car=mahindra)
# bolero = CarModel.objects.create(name="Bolero", car=mahindra)


# carmodel se car fetch 
# thar = CarModel.objects.get(name="thar")
# print(thar.car)          # get car name


# car se carmodel fetch 
# a1 = Car.objects.get(name="Mahindra")
# print(a1.carmodel_set.all())        # related_name not provided then use

# print(a1.cmodel.all())       # related_name provided then use -- fetch all carmodel


# for car_model in CarModel.objects.all():
#     print(car_model)           # related_name provided then use -- fetch all carmodel


# add Honda CarModels 
# honda = Car.objects.get(name='Honda')
# amaze = CarModel.objects.create(name="Amaze", car=honda)
# hondacity = CarModel.objects.create(name="Honda-City", car=honda)


# model = CarModel.objects.filter(car__name="Honda")
# print(model)            # fetch car model by Honda


# cmodel = CarModel.objects.filter(car__name__in=["Mahindra", "Honda"])
# print(cmodel)               # fetch both cars Models


# for i in CarModel.objects.filter(car__name="Honda"):
#     print(i)                 # fetch car model by Honda

# for cmodel in CarModel.objects.filter(car__name="Mahindra"):
#     print(cmodel)             # fetch car model by Mahindra


# try kraych 

# honda = Car.objects.get(name="Honda")
# print(honda.car_set.all())

# try kraych 


# Car.objects.get(name="HOnda").delete()     # delete car




from relationship.models import *

# swift = FourWheeler.objects.create(name="Swift")
# innova = FourWheeler.objects.create(name="Innova")


# cng = FuelType.objects.create(name="CNG")
# diesel = FuelType.objects.create(name="Diesel")
# hybrid = FuelType.objects.create(name="Hybrid")


# innova = FourWheeler.objects.get(name="Innova")
# print(swift)      # get the car

# hybrid = FuelType.objects.get(name="Hybrid")

# innova.fueltype.add(hybrid)
# print(innova.fueltype.all())

# newcar = FourWheeler.objects.create(name="Thar")

thar = FourWheeler.objects.get(name="Thar")     # create a fuel type and assign
thar.fueltype.create(name="Petrol")

# diesel = FuelType.objects.get(name="Diesel")
# print(diesel.fourwheeler_set.all())            # fetch car
# print(diesel.cmodels.all())

# all = FourWheeler.objects.filter(fueltype__name__startswith="D")
# print(all)


# remove fueltype 
# --------------------
# petrol = FuelType.objects.get(name="Petrol")
# thar = FourWheeler.objects.get(name="Thar")   
# thar.fueltype.remove(petrol)
# -----------------------

# ERD = Entity Realational Diagram 


