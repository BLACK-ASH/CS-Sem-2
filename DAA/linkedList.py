# Making The Class Node
class Node:
    # Initalizing The Class
    def __init__(self,data,nextNode=None):
        self.data = data
        self.nextNode = nextNode

    # Getting The Data
    def getData(self):
        return self.data

    # Setting The Data
    def setData(self,data):
        self.data = data

    # Getting The Next Node
    def getNextNode(self):
        return self.nextNode

    # Setting The Next Node
    def setNextNode(self,reference):
        self.nextNode = reference

# Making The Linked List Class
class LinkedList:
    # Initalizing The Class
    def __init__(self,head = None):
        self.head = head
        self.size = 0

    # Getting The Size Of The Linked List
    def getSize(self):
        return self.size

    # Adding A Node In A Linked List
    def addNode(self,data):
        newNode = Node(data,self.head)
        self.head = newNode
        self.size += 1
        return True

    # Adding A Node In A Certain Position In A Linked List
    def addNodeAtPos(self, data, pos):
        if pos < 0:
            print("Position cannot be negative")
            return False
        newNode = Node(data)
        if pos == 0:
            newNode.nextNode = self.head
            self.head = newNode
        else:
            currentNode = self.head
            currentPosition = 0
            while currentNode and currentPosition < pos - 1:
                currentNode = currentNode.nextNode
                currentPosition += 1
    
            if currentNode is None:
                print("Position is out of range")
                return False
            newNode.nextNode = currentNode.nextNode
            currentNode.nextNode = newNode
            self.size += 1
            return True
       

    # Printint The Node
    def printNode(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.getNextNode()

    # Deleting A Node
    def deleteNode(self,key):
        temp = self.head
        if (temp is not None):
            if (temp.data == key):
                self.head == temp.nextNode
                temp = None
                return
        while (temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.nextNode
        if (temp == None):
            return
        prev.nextNode = temp.nextNode
        temp = None
        self.size -= 1
        return True

    # Maximum In A List
    def maximum(self):
        curr = self.head
        maxElement = curr.data
        while curr:
            if maxElement < curr.data:
                maxElement = curr.data
            curr = curr.getNextNode()
        return maxElement

    # Minimum In A List
    def minimum(self):
        curr = self.head
        minElement = curr.data
        while curr:
            if minElement > curr.data:
                minElement = curr.data
            curr = curr.getNextNode()
        return minElement

mylist = LinkedList()
mylist.addNode(40)
mylist.addNode(4)
mylist.addNode(14)
mylist.addNodeAtPos(55,3)
mylist.addNode(24)
mylist.addNode(34)
mylist.printNode()
print("The Largest Number  In A List Is : ",mylist.maximum())
print("The Smallest Number  In A List Is : ",mylist.minimum())
print("The Difference In Largest And Smallest In A List : ",mylist.maximum()-mylist.minimum())
