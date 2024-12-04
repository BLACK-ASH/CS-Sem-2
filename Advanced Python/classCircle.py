#---------------------------------------Class--------------------------------------#
# Creating Class Of Circle
class Circle:
    radius=0
    circumference=0
    area=0

    #Circumference Of Circle
    def circumferenceOfCircle(this):
       this.circumference = 2 * 3.14 * this.radius
       return 2 * 3.14 * this.radius

    #Area Of Circle
    def areaOfCircle(this):
        this.area = 3.14 * (this.radius ** 2)
        return 3.14 * (this.radius ** 2)

    #Display Curcumference
    def displayCircumference(this):
        print(this.circumference)
        
    #Display Area
    def displayArea(this):
        print(this.area)

#----------------------------------------Code--------------------------------------#

# Making Object
abc = Circle()

# User choice
choice = "y"

while choice == "y":
    # Giving Radius To Object
    abc.radius = int(input("Enter Radius : "))

    #Calling Function To Calculate Area And Circumference
    abc.circumferenceOfCircle()
    abc.areaOfCircle()

    # Printin Radius,Curcumference , Area
    print ("Circumference Of Circle")
    abc.displayCircumference()
    print("Area Of Circle")
    abc.displayArea()

    # Asking User If Wants To Continue
    choice = input("Want To Continue : ")
