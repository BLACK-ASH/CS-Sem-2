# Deleting A Node
    def deleteNode(self, key):
        temp = self.head
        if temp is not None and temp.data == key:
            self.head = temp.nextNode
            temp = None
            self.size -= 1
            return  False # <--- Add this line

        prev = None
        while temp is not None:
            if temp.data == key:
                prev.nextNode = temp.nextNode
                temp = None
                self.size -= 1
            else:
                prev = temp
            temp = temp.nextNode