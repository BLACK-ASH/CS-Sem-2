# Base Class
class Parent():
    def callParent(self):
        print("This Is The Class Of Parent.")

# Child Class
class Child1(Parent):
    def callChild(self):
        print("This Is The Class Of Child 1.")

# Child Class
class Child2(Parent):
    def callChild(self):
        print("This Is The Class Of Child 2.")

# Child Class
class Child3(Parent):
    def callChild(self):
        print("This Is The Class Of Child 3.")

# Child Class
class Child4(Parent):
    def callChild(self):
        print("This Is The Class Of Child 4.")


# Creating The Object
obj1 = Child1()
obj2 = Child2()
obj3 = Child3()
obj4 = Child4()

# Calling The Object
obj1.callParent()
obj1.callChild()

obj2.callParent()
obj2.callChild()

obj3.callParent()
obj3.callChild()

obj4.callParent()
obj4.callChild()
