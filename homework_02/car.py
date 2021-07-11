"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02.base import Vehicle


class Car(Vehicle):
    def __init__(self):
        super(Car, self).__init__()
        self.engine = None

    def set_engine(self, engine):
        self.engine = engine
