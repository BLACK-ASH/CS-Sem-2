# Multiple Inheritance
# First Class
class Mother:
    motherName = ""
    def motherNameDisplay(self):
        return self.motherName

# Second Class
class Father:
    fatherName = ""
    def fatherNameDisplay(self):
        return self.fatherName

# Third Class
class Child(Mother,Father):
    def getParents(self):
        print("My Mother Is : ",self.motherNameDisplay())
        print("My Father Is : ",self.fatherNameDisplay())

# Calling Class

son = Child()

son.motherName = "Jane Doe"
son.fatherName = "John Doe"

son.getParents()
