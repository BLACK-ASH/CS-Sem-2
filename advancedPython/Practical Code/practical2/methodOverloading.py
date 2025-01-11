
class Example:
    def add(self,a=None,b=None,c=None):
        x=0
        if a and b and c != None :
            x = a+b+c
        elif a and b != None and c == None:
            x = a+b
        return x

obj = Example()
print(obj.add(10,20,30))
print(obj.add(10,20))
