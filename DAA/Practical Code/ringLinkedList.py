class Ring:
    def __init__(self,data):
        if not len(data):
            raise "Ring Must Have At Least One Element."
        self._data = data

    def repr(self):
        return repr(self._data)

    def length(self):
        return len(self._data)

    def getItem(self,key):
        return self._data[key]

    def turn(self):
        last = self._data.pop(-1)
        self._data.insert(0,last)
        return True

    def first(self):
        return self._data[0]

    def last(self):
        return self._data[-1]

    def remove(self,key):
        return self._data.pop(key)

    def add(self,data):
        self._data.append(data)
        return True

    
ring = Ring(["Ashif","Arshad","Raza","Harsh","Farhan","Harish","Sachin"])

print(ring.repr())
print(ring.first())   
print(ring.last())

ring.turn()
print("After Turn")
print(ring.repr())

print("The Size Of The Ring Linked List Is ",ring.length())

print("The Element At Position 3 Is",ring.getItem(3))
print("The Element At Position 5 Is",ring.getItem(5))

print("Element Before Adding")
print(ring.repr())
ring.add("test")
print("Element After Adding")
print(ring.repr())

print("Element Before Deleting")
print(ring.repr())
ring.remove(-1)
print("Element After Deleting")
print(ring.repr())
