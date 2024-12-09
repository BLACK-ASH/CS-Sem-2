# Creating Default Constructor
class Car :
    def __init__(self):
        self.name = "BMW"
        self.model = "X1"
        self.year = 2020

car = Car()

print("-------------------------------------------------------------")
print("Default Constructor")
print("-------------------------------------------------------------")
print(car.name)
print(car.model)
print(car.year)
# Updating Value
car.name = "Audi"
print(car.name)


print("-------------------------------------------------------------")
print("Parameterized Constructor")
print("-------------------------------------------------------------")
# Creating Parameterized Constructor
class Car :
    def __init__(self,name,model,year):     
        self.name = name
        self.model = model
        self.year = year
    def display(self):
        print("Car Name : %s\nCar Model : %s\nCar Year : %d"%(self.name,self.model,self.year)) 

car = Car("BMW","X1",2020)

print("------------------------Normal Display-----------------------")
print(car.name)
print(car.model)    
print(car.year) 
print("----------------Through Display Function---------------------")

car.display()

# Creating Destructor
print("-------------------------------------------------------------")
print("Destructor")
print("-------------------------------------------------------------")
class Car :
    def __init__(self,name,model,year):     
        self.name = name
        self.model = model
        self.year = year

    def __del__(self): # Destructor
        print("Object Destroyed")

car = Car("BMW","X1",2020)
print(car.name)
print(car.model)    
print(car.year)

del car