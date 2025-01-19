class Node:
    def __init__(self,data,nextNode=None,prevNode=None):
        self.data = data
        self.nextNode = nextNode
        self.prevNode = prevNode

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def push(self,data):
        newNode = Node(data)
        newNode.nextNode = self.head
        
        if self.head is not None:
            self.head.prevNode = newNode

        self.head = newNode

        return True

    def insert(self,key,data):
        curr = self.head
        
        # To Handling Base Case
        if curr.data == key:
            self.push(data)
            return True

        # To Find The Target Node
        while curr:
            if curr.data == key:
                target = curr
                break
            curr = curr.nextNode 

        # To Check The Target
        if target is None:
            print("The Previous Node Cannot Be Null.")
            return False

        # Creating New Node
        newNode = Node(data)

        # Setting Next Node
        if target.prevNode is not None:
            target.prevNode.nextNode = newNode
        newNode.nextNode = target

        # Setting Previous Node
        newNode.prevNode = target.prevNode
        target.prevNode = newNode

        return True
        
    def printList(self):
        curr = self.head

        while curr:
            print(curr.data,end=" --> ")
            curr = curr.nextNode
        print("None")

#  Creating The List And Adding Elements
l = DoubleLinkedList()
l.push(1)
l.push(3)
l.push(4)
l.push(5)

# Inserting Element
print("Before Inserting Element")
l.printList()
l.insert(1,2)
print("After Inserting Element")
l.printList()

# Checking Funtion If It Works For Base Case
l.insert(5,6)
l.printList()
