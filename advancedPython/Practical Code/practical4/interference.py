from abc import ABC,abstractmethod
class Area(ABC):
    @abstractmethod
    def findArea(self):
        pass

class Triangle(Area):
    def __init__(self,height,breadth):
        self.h  = height
        self.b = breadth

    def findArea(self):
        return 1/2 * self.h * self.b

class Rectangle(Area):
    def __init__(self,length,breadth):
        self.l  = length
        self.b = breadth

    def findArea(self):
        return self.l * self.b

t = Triangle(10,20)
print(t.findArea())

r = Rectangle(10,20)
print(r.findArea())
