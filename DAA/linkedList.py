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
    def addNodeAtPos(self,data,pos):
        newNode = Node(data,pos)
        currentNode = self.head
        currentPosition = 0
        while True:
            if currentPosition == pos:
                previousNode.nextNode = newNode
                newNode.nextNode = currentNode
                self.size += 1
                return True
            else:
                previousNode = currentNode
                currentNode = currentNode.nextNode
                currentPosition += 1

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
               
                
                
