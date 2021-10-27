from django.test import TestCase, Client

from Employees.views import CreateEmployeeView, CreatePersonView

# Create your tests here.
from Employees.models import Person, Employee


class TestPersons(TestCase):
    def setUp(self):
        self.employee = Employee.objects.create(position='Programmer', department='Multimedia', salary=150)
        self.person = Person.objects.create(firstName='Kirill',
                                       lastName='Popov',
                                       birthday='1991-08-06',
                                       started_at='2015-02-06',
                                       employee=self.employee)

        print('Employee and Person created')

    def tearDown(self) -> None:
        self.employee.delete()
        self.person.delete()
        print('Employee and person deleted')
