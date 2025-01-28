class Queue:
    def __init__(self):
        self.queue = []

    def enque(self,data):
        self.queue.append(data)
        return True

    def deque(self):
        self.queue.pop(0)
        return True

    def isEmpty(self):
        return len(self.queue)==0

    def length(self):
        return len(self.queue)

    def print(self):
        print(self.queue)

queue = Queue()

# Adding Elements
queue.enque(1)
queue.enque(2)
queue.enque(3)
queue.enque(4)
queue.enque(5)
queue.print()

# Removing Elements
queue.deque()
queue.deque()
queue.deque()
queue.print()

# Checking If Queue Is Empty And Length Of Queue
print(queue.isEmpty())
print(queue.length())