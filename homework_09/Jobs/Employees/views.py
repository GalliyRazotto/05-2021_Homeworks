from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from Employees.models import Person, Employee, Project
# Create your views here.


class PersonList(ListView):
    model = Person


class PersonView(DetailView):
    model = Person


class CreateEmployeeView(CreateView):
    model = Employee
    fields = ('position', 'department', 'salary')
    success_url = reverse_lazy('list')


class CreatePersonView(CreateView):
    model = Person
    fields = ('firstName', 'lastName', 'birthday', 'started_at', 'employee')
    success_url = reverse_lazy('list')



