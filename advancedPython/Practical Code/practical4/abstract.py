from abc import ABC,abstractmethod

class Animal(ABC):
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Bark"

dog = Dog()
print(dog.sound())

