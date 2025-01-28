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
