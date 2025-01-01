# Base Class
class Grandfather:
    def __init__(self,grandFatherName):
        self.grandFatherName = grandFatherName

# Intermidiate Class
class Father(Grandfather):
    def __init__(self,fatherName,grandFatherName):
        self.fatherName = fatherName
        # Invoking Constructor Of GrandFather
        Grandfather.__init__(self,grandFatherName)

# Derived Class
class Son(Father):
    def __init__(self,sonName,fatherName,grandFatherName):
        self.sonName = sonName

        # Invoking Constructor Of Father
        Father.__init__(self,fatherName,grandFatherName)

    def displayFamily(self):
        print("My Name Is : ",self.sonName)
        print("My Father Name Is : ",self.fatherName)
        print("My GrandFather Name Is : ",self.grandFatherName)

# Calling Class
family = Son("Himesh","Dipesh","Alpesh")

print(family.grandFatherName)

family.displayFamily()
