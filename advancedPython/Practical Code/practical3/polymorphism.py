class Duck:
    def swim(self):
        print("I Am A Duck I Can Swim.")

class Sparrow:
    def swim(self):
        print("I Am A Sparrow I Can't Swim,But I Can Fly.")

class Crocodile:
    def swim(self):
        print("I Am A Crocodile I Can Swim And Walk.")

def callFunction(obj):
    obj.swim()

callFunction(Duck())
callFunction(Sparrow())
callFunction(Crocodile())

