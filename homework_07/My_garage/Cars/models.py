from django.db import models
# Create your models here.


class Manufacture(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)


class Car(models.Model):
    car = models.CharField(max_length=64, default='')
    carManufacture = models.ForeignKey(
        Manufacture,
        on_delete=models.CASCADE,
    )


class Employee(models.Model):
    id = models.OneToOneField(Manufacture, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
