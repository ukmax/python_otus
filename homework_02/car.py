"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02.base import Vehicle


class Car(Vehicle):
    engine = None

    def set_engine(self, new_engine):
        self.engine = new_engine
