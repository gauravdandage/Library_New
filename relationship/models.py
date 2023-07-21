from django.db import models

# Create your models here.


class Person(models.Model):       # person_object.aadhar
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    mobile = models.BigIntegerField(null=True, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "person"


class Aadhar(models.Model):      # aadhar_object.person
    aadhar_number = models.BigIntegerField(unique=True)
    address = models.CharField(max_length=250)
    creation_date = models.DateTimeField(auto_now=True)
    DOB = models.DateField()
    person = models.OneToOneField(Person, on_delete=models.CASCADE, null=True)     # Person class
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.aadhar_number)

    class Meta:
        db_table = "aadhar"






class Car(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "car"


class CarModel(models.Model):
    name = models.CharField(max_length=255)
    car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True, related_name="cmodel")
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = "car_model"

   
# ---------------------------------------------------------------------------------------------


class FuelType(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = "fuel_type"
    
    
class FourWheeler(models.Model):
    name = models.CharField(max_length=255)
    # fueltype = models.ManyToManyField(FuelType, related_name="cmodels")

    # def __str__(self):
    #     return self.name

    # class Meta:
    #     db_table = "fourwheelers"


# ERD = Entity Realational Diagram 

# composite key 
# substitute for ManyToManyField 
class CModel_Fueltype(models.Model):
    cmodel = models.ForeignKey(FourWheeler, on_delete=models.SET_NULL, null=True)
    fueltype = models.ForeignKey(FuelType, on_delete=models.SET_NULL, null=True)
    extra_field = models.CharField(max_length=225)

    class Meta:
        unique_together = (("cmodel", "fueltype"),)      # composites key








