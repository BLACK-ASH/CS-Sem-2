class Employee:
    def __init__(self,id,name):
        self.id = id
        self.name = name

    def display(self):
        print("Employee ID : ",self.id)
        print("Employee Name : ",self.name)

n = int(input("Enter The Number Of Employee : "))

while 1 > n:
    n= int(input("Enter A Positive Number : "))

employees = []

for i in range (n):
    print("Enter The Information Of Employee No ",i+1)
    id = input("Enter The Id : ")
    name = input("Enter The Name : ")
    employees.append(Employee(id,name))

for emp in employees:
    emp.display()
