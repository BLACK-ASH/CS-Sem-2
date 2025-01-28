class Stack:
    def __init__(self):
        self.stack = []

    def push(self,data):
        self.stack.append(data)
        return True

    def pop(self):
        if not self.isEmpty:
            self.stack.pop(-1)
        return True

    def isEmpty(self):
        return len(self.stack)==0

    def length(self):
        return len(self.stack)

    def print(self):
        print(self.stack)


str = input("Enter Equation To Check It Is Correct : ")


def check(str):
    test = Stack()
    for e in str:
        if e in ["[","{","(","]","}",")"]:
            test.push(e)
        elif e in ["]","}",")"]:
            test.pop()

    print(test.isEmpty())

            
            
        
