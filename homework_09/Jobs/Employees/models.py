from django.db import models

# Create your models here.


class Employee(models.Model):
    position = models.TextField()
    department = models.TextField()
    salary = models.PositiveIntegerField()


class Person(models.Model):
    firstName = models.TextField()
    lastName = models.TextField()
    birthday = models.DateField()
    started_at = models.DateField(auto_created=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)


class Project(models.Model):
    projectName = models.TextField(default='New project')
    dataStart = models.DateTimeField(auto_now_add=True)
    personInUse = models.ManyToManyField(Person)
