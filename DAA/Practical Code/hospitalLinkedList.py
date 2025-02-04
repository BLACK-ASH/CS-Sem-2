class Patient:
    def __init__(self,bedNo,name,age,disease,reports = ""):
        self.bedNo = bedNo
        self.data = {
            "name":name,
            "age":age,
            "disease" : disease,
            "reports" : reports
            }
        self.next = None

class PatientList:
    def __init__(self,deptName,maxBed):
        if maxBed <= 0:
            print("Beds Cannot Be Negative Or Zero")
            return False
        self.head = None
        self.__maxBed = maxBed
        self.deptName = deptName
        self.__bedOccupied = 0
        self.__bedsOccupied = []

    def bedEmpty(self):
        return self.__maxBed > self.__bedOccupied

    def __getPatient(self,key):
        target = self.head
        while target:
            if target.bedNo == key:
                return target
            target = target.next
        return None

    def __giveBedNo (self):
        if len(self.__bedsOccupied) == 0:
            return 1

        if len(self.__bedsOccupied) == 1:
            return 2

        
        self.__bedsOccupied.sort()
        i = 0
        while i < len(self.__bedsOccupied)-1:
            if self.__bedsOccupied[i+1]-self.__bedsOccupied[i] > 1:
                return i + 1 + 1
            i+=1

        return self.__bedsOccupied[-1] + 1

    def insert(self,name,age,disease,reports,bedNo):
        if self.head == None:
            patient = Patient(bedNo,name,age,disease,reports)
            patient.next = self.head
            self.head = patient
            return True
        
        if bedNo >= self.head.bedNo:
            patient = Patient(bedNo,name,age,disease,reports)
            patient.next = self.head
            self.head = patient
            return True
        
        curr=self.head
        prev = self.head
        while curr:
            if curr.bedNo <= bedNo:
                break
            prev = curr
            curr = curr.next
            
            
        patient = Patient(bedNo,name,age,disease,reports)
        patient.next = prev.next
        prev.next = patient
        return True

    def isBedAvailable(self,bedNo):
        if bedNo == None:
            return False
        if bedNo > self.__maxBed and bedNo <0:
            return False
        return bedNo not in self.__bedsOccupied
        
    def admit(self,name,age,disease,reports,bedNo = None):
        # If There Is No Bed To Admit
        if not self.bedEmpty():
            print("All Beds Are Occupied.")
            return False

        # If Bed No Is Given
        if bedNo:
            # Checking If Bed Is Available
            if not self.isBedAvailable(bedNo):
                print("Bed Not Available")
                beds = list(range(1,self.__maxBed+1))
                availableBed = list(set(beds)  - set(self.__bedsOccupied))
                print("The Following Beds Are Available")
                print(availableBed)
                return False

            # Admiting Patient:
            self.__bedOccupied+=1
            self.insert(name,age,disease,reports,bedNo)
            self.__bedsOccupied.append(bedNo)
            
            return True
            
        # Giving Bed No
        if bedNo == None:
            bedNo = self.__giveBedNo()

        self.__bedOccupied+=1
        self.insert(name,age,disease,reports,bedNo)
        self.__bedsOccupied.append(bedNo)
        
        return True

    def discharge(self,bedNo):
        curr=self.head
        prev = self.head
        while curr and prev:
            if curr.bedNo == bedNo:
                break
            prev = curr
            curr = curr.next

        prev.next = curr.next
        curr = None
        self.__bedsOccupied.remove(bedNo)
        self.__bedOccupied -=1
        
        return True

    def getPatientDetails(self,bedNo):
        patient = self.__getPatient(bedNo)
        print(patient.data)
        

    def print(self):
        print("Department Name : ",self.deptName)
        target = self.head
        while target:
            print({"BedNo" : target.bedNo,"Name" : target.data["name"]})
            target = target.next
        

# Creating Department
l = PatientList("ENT",5)

# Admiting Patinet
l.admit("John Doe",25,"abc","abc")
l.admit("John Doe ka bhai",27,"abcd","abcd")

# Admiting Patinet By Bed NO
l.admit("Jane Doe",29,"cd","cd",5)
l.print()

# Handling If Bed Not Available
l.admit("Jane Doe 2",29,"cd","cd",5)
l.admit("Jane Doe 2",29,"cd","cd")
l.print()
l.admit("Jane Doe 2",29,"cd","cd")
l.print()

# Getting Patient Details
l.getPatientDetails(2)

# Discharge
l.discharge(2)
l.print()
l.admit("Jane Doe 3",29,"cd","cd")
l.print()
