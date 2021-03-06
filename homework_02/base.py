from abc import ABC
from homework_02 import exceptions


class Vehicle(ABC):
    def __init__(self, weight=0, fuel=0, fuel_consumption=0):
        self.weight = weight
        self.started = False
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = not self.started
            else:
                raise exceptions.LowFuelError('Low Fuel Error')

    def move(self, distance):
        fuel_needed = self.fuel_consumption*distance
        if fuel_needed <= self.fuel:
            self.fuel -= fuel_needed
        else:
            raise exceptions.NotEnoughFuel('Not Enough Fuel')
