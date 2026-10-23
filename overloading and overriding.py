#overloading

class Addition:
    def add(self, a, b=0, c=0):
        print("Sum =", a + b + c)

obj = Addition()

obj.add(10)
obj.add(10, 20)
obj.add(10, 20, 30)

 #overriding

class Parent:
    def show(self):
        print("This is the parent class")

class Child(Parent):
    def show(self):  
        print("This is the child class")

obj = Child()
obj.show()
