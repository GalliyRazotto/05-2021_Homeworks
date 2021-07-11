"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02 import exceptions


class Plane(Vehicle):
    def __init__(self, weight, fuel, fuel_consumption, cargo=0, max_cargo=0):
        super(Plane, self).__init__(weight, fuel, fuel_consumption)
        self.cargo = cargo
        self.max_cargo = max_cargo

    def load_cargo(self, load_cargo):
        sum_cargo = self.cargo + load_cargo
        if sum_cargo <= self.max_cargo:
            self.cargo = sum_cargo
        else:
            raise exceptions.CargoOverload('Cargo Overload')

    def remove_all_cargo(self):
        last_cargo = self.cargo
        self.cargo = 0
        return last_cargo
