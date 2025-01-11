# Creating Parent Class
class School:
    def schoolName(self):
        print("This is a school")
 
# Creating Child Class       
class Student1(School):
    def studentName(self):
        print("This is a student1")
        
class Student2(School):
    def studentName(self):
        print("This is a student2")
        
class Student3(School, Student1, Student2):
    def studentName(self):
        print("This is a student3")
    

# Creating Object And Calling The Method
s1 = Student1()
s1.studentName()
s1.schoolName()

s2 = Student2()
s2.studentName()
s2.schoolName()

s3 = Student3()
s3.studentName()
s3.schoolName()