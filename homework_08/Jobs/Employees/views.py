from django.shortcuts import render
from Employees.models import Person, Employee, Project
# Create your views here.


# Display Persons
def index_persons(request):
    persons = Person.objects.all()
    return render(request,
                  'employees/index_persons.html',
                  {'persons': persons})


# Detailed view
def detailed_view(request, person_id):
    person = Person.objects.filter(pk=person_id).first()
    return render(request,
                  'employees/employee_detail.html',
                  {'person': person})
