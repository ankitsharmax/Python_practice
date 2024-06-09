class Animal:
    def eat(self):
        print("eating..")

class Dog(Animal):
    def bark(self):
        print("barking..")

dog = Dog()
dog.eat()
dog.bark()