class Base:
    def __init__(self,data):
        self.data = data

    def __add__(self,other):
        return self.data + other.data
    
obj = Base(10)
obj2 = Base(20)
print(obj+obj2)
        
fName = input("Enter the first name: ")
lName = input("Enter the last name: ")
print(fName + " " + lName)