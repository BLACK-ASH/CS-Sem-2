class Parent:
    def __init__(self):
        self.name = "Parent"
    
    def call(self):
        print("I Am Inside ", self.name)

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.name = "Child"
    
    def call(self):
        print("I Am Inside ", self.name)
        
parent = Parent()
parent.call()
child = Child()
child.call()