# Creating List Of Employees
employees = []

# Creating Employee Class
class Employee:
    def __init__(self,name):
        # Auto Id
        count=len(employees)
        self.id = "emp"+ str(count)
        self.name = name

    def display(self):
        print("ID : %s\nName : %s"%(self.id,self.name))

    def __del__(self):
        print("Object Destroyed")

# Taking Choice
choice = "y"

# Creating Input Function For Employee
def employeeInput():
    # Taking Input For Number Of Employees
    numOfEmployees = 0

    # Handling Invalid Input
    while numOfEmployees < 1:
      numOfEmployees = int(input("Enter Number Of Employees : "))

    # Taking Input For Each Employee
    for i in range(numOfEmployees):
        print("Employee %d"%(i+1))
        name = input("Enter Name : ")
        employees.append(Employee(name))

    # Displaying Each Employee
    for employee in employees:
        employee.display()

    # Asking If User Wants To Continue
    global choice
    choice = input("Enter Your Choice (y/n) : ").lower()

# Taking User Choice If He/She Wants To Continue
while "y"== choice:
    employeeInput()