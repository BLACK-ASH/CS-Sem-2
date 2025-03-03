# Making The Class Node
class Node:
    # Initalizing The Class
    def __init__(self,customer,salesman,nextNode=None):
        self.data = {
            "customer":customer,
            "salesman":salesman
            }
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
    def addCustomer(self,customer,salesman):
        newNode = Node(customer,salesman,self.head)
        self.head = newNode
        self.size += 1
        return True

    # Adding A Node In A Certain Position In A Linked List
    def addCustomerAtPos(self,customer,salesman,pos):
        newNode = Node(customer,salesman,pos)
        previousNode = None
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
    def printCustomer(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.getNextNode()

    # Deleting A Customer
    def deleteCustomer(self,key):
        temp = self.head
        if (temp is not None):
            if (temp.data["customer"] == key):
                self.head = temp.nextNode
                temp = None
                return
        while (temp is not None):
            if temp.data["customer"] == key:
                break
            prev = temp
            temp = temp.nextNode
        if (temp == None):
            return
        prev.nextNode = temp.nextNode
        temp = None
        self.size -= 1

    # Find Customer By Salesman
    def customerBySalesman(self,key):
        curr = self.head
        data = {
                "salesman":key,
                "customers":[]
            }
        while curr:
            if curr.data.get("salesman") == key:
                data["customers"].append(curr.data.get("customer"))
            curr = curr.getNextNode()
               
        return data

    # Find Salesman By Customer
    def salesmanrByCustomer(self,key):
        curr = self.head
        data = {
                "customers":key,
                "salesman":""
            }
        while curr:
            if curr.data.get("customer") == key:
                data["salesman"]=curr.data.get("salesman")
            curr = curr.getNextNode()
               
        return data



# Running The Code
myList = LinkedList()

myList.addCustomer("Arshad","Huzaifa")
myList.addCustomer("Arshad","Huzaifa")
myList.addCustomer("Ashif","Huzaifa")
myList.addCustomer("Harsh","Huzaifa")

print("All Customer With Salesman")
myList.printCustomer()

print("Find Customer By Salesman")
print(myList.customerBySalesman("Huzaifa"))

print("Find Salesman By Customer")
print(myList.salesmanrByCustomer("Ashif"))

