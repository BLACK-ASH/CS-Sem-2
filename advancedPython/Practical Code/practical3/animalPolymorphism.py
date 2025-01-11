class Dog:
    def tellAboutYou(self):
        print("I am a dog, I am from Kingdom Animalia and from sub-kingdom Mammalia")
    def limbs(self):
        print("I have 4 limbs")
        
class Lizard:
    def tellAboutYou(self):
        print("I am a lizard, I am from Kingdom Animalia and from sub-kingdom Reptilia")
    def limbs(self):
        print("I have 4 limbs")
        
def printObject(obj):
    obj.tellAboutYou()
    obj.limbs()
    
d = Dog()
l = Lizard()

printObject(d)
printObject(l)