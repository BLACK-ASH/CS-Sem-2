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

        i = 0
        while i < len(self.__bedsOccupied)-1:
            if self.__bedsOccupied[i+1]-self.__bedsOccupied[i] > 1:
                return i + 1 + 1
            i+=1

        return self.__bedsOccupied[-1] + 1

    def insert(self,name,age,disease,reports,bedNo):
        print(bedNo)
        if self.head == None:
            patient = Patient(bedNo,name,age,disease,reports)
            patient.next = self.head
            self.head = patient
            return True
        
        if bedNo-1 == self.head.bedNo:
            patient = Patient(bedNo,name,age,disease,reports)
            patient.next = self.head
            self.head = patient
            return True
        
        curr=self.head
        nextNode = self.head.next
        while curr and nextNode:
            if curr.bedNo == bedNo:
                break
            curr = nextNode
            nextNode = nextNode.next
            
        patient = Patient(bedNo,name,age,disease,reports)
        curr.next = patient
        patient.next = nextNode
        return True

    def isBedAvailable(self,bedNo):
        if bedNo == None:
            return False
        if bedNo > self.__maxBed and bedNo <0:
            return False
        return bedNo not in self.__bedsOccupied

    def insert(self,,name,age,disease,reports,bedNo):
        if bedNo

        
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
        

    def print(self):
        target = self.head
        while target:
            print({"BedNo" : target.bedNo,"Name" : target.data["name"]})
            target = target.next
        


        
