#2
#inher
#overloading
#super
#3
#poly
#duck
#overrinding

class Example:
    def add(self,a,b,c=None):
        x=0
        if a and b and c != None :
            x = a+b+c
        elif a and b != None and c == None:
            x = a+b
        return x

obj = Example()
print(obj.add(10,20,30))
print(obj.add(10,20))
