class MethodOverloading:
    def __init__(self):
        print("Object Created")

    def add(self,a:int,b:int) -> int:
        print(f"{a} + {b} = {a + b}")

    def add(self,a:float,b:float) -> float:
        print(f"{a} + {b} = {a + b}")

    def hello(self,a,b,c=None):
        if c is not None:
            print(a,b,c)
        else:
            print(a,b)



methodoverloading = MethodOverloading()
methodoverloading.add(2,4)
methodoverloading.add(2.0,4.0)
methodoverloading.hello("Naruto","Sasuke")
methodoverloading.hello("Naruto","Sasuke","Kakashi")