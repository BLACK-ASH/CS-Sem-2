# Single Inheritance
# # First Class
class Parent:
    def func1(self):
        print("This function is in parent class.")

# Second Class
class Child(Parent):
    def func2(self):
        print("This function is in child class.")

# Calling Class
object = Child()

object.func1()
object.func2()
