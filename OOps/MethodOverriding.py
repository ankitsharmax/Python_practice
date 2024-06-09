class Vehicle:
    def run(self):
        print("Vehicle running..")

class Bike(Vehicle):
    def run(self):
        print("Bike running..")

bike = Bike()
bike.run()