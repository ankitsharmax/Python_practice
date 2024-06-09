class Animal:
    def eat(self):
        print("Eating..")

class Dog(Animal):
    def bark(self):
        print("Barking..")

class BabyDog(Dog):
    def play(self):
        print("Playing..")

babydog = BabyDog()
babydog.eat()
babydog.bark()
babydog.play()