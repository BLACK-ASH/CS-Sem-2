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

    def insert(self,prevNode,data):
        curr = self.head
        while curr:
            if curr.data == prevNode:
                prevNode = curr
                break
            curr = curr.nextNode 
        
        if prevNode is None:
            print("The Previous Node Cannot Be Null.")
            return False
        newNode = Node(data)

        newNode.prevNode = prevNode
        prevNode.nextNode = newNode

        return True
        
    def printList(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.nextNode 
