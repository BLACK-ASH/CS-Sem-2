# Creating Employee Class
class Employee:
    def __init__(self,id,name):
        self.id = id    
        self.name = name

    def display(self):
        print("ID : %d\nName : %s"%(self.id,self.name))

    def __del__(self):
        print("Object Destroyed")

# Taking Input For Number Of Employees
numOfEmployees = 0

# Handling Invalid Input
while numOfEmployees < 1:
   numOfEmployees = int(input("Enter Number Of Employees : "))

# Creating List Of Employees
employees = []

# Taking Input For Each Employee
for i in range(numOfEmployees):
    print("Employee %d"%(i+1))
    id = int(input("Enter ID : "))
    name = input("Enter Name : ")
    employees.append(Employee(id,name))

# Displaying Each Employee
for employee in employees:
    employee.display()