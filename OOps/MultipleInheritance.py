class Calculator1:
    def add(self,a,b):
        print(f"{a} + {b} = {a+b}")

class Calculator2:
    def sub(self,a,b):
        print(f"{a} - {b} = {a - b}")

class Calculator(Calculator1,Calculator2):
    def mul(self,a,b):
        print(f"{a} * {b} = {a * b}")

calculator = Calculator()
calculator.add(2,4)
calculator.sub(2,4)
calculator.mul(2,4)