# Without Using Threading
class A:
    def run(self):
        for i in range(5):
            print("John Doe")

class B:
    def run(self):
        for i in range(5):
            print("Jane Doe")

obj1=A()
obj2=B()

print("Without Using Threading")
obj1.run()
obj2.run()

# Using Threading
from time import sleep
from threading import Thread

class A(Thread):
    def run(self):
        for i in range(5):
            print("John Doe (Thread)")
        sleep(1)

class B(Thread):
    def run(self):
        for i in range(5):
            print("Jane Doe (Thread)")
        sleep(1)
        
objT1=A()
objT2=B()

print("Using Threading")
objT1.run()
objT2.run()

