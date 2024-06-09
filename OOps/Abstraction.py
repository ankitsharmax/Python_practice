'''
Python has no inbuilt functionality for the abstarct class implementation therefore we use abc module to implement it.
'''
from abc import ABC

class Car(ABC):
    def brand(self):
        pass

class Tesla(Car):
    def brand(self):
        print("Tesla")

class Suzuki(Car):
    def brand(self):
        print("Suzuki")

tesla = Tesla()
tesla.brand()

suzuki = Suzuki()
suzuki.brand()
