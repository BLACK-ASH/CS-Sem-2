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
        i = 0
        
        if len(self.__bedsOccupied) <= 2:
            return len(self.__bedsOccupied)+1
        
        while i <= self.__maxBed:
            if self.__bedsOccupied[0]-self.__bedsOccupied[i+1] > 1:
                return i + 1

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
            target = self.head
            prev = None
            while target:
                if target.bedNo == bedNo:
                    break
                prev = target
                target = target.next
            
            patient = Patient(bedNo,name,age,disease,reports)
            if target and prev:
                prev.next = patient
                patient.next = target
                return True
            
        # Giving Bed No
        if bedNo == None:
            bedNo = self.__giveBedNo()
        self.__bedsOccupied.append(bedNo)

        # Creating Patient
        patient = Patient(bedNo,name,age,disease,reports)
        patient.next = self.head
        self.head = patient
        self.__bedOccupied +=1

        return True

    def print(self):
        target = self.head
        while target:
            print({"BedNo" : target.bedNo,"Data" : target.data})
            target = target.next
        


        
