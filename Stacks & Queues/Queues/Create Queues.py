class Queues:

    def __init__(self):

        self.queues = []
        self.front = -1
        self.rear = -1

    def enqueue(self, element):

        if self.front == -1:

            self.front = self.front+1
            self.rear = self.rear+1

        else:
            self.rear = self.rear+1

        self.queues.append(element)

    def dequeue(self):

        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = self.front+1


obj = Queues()
obj.enqueue(1)
obj.enqueue(5)
obj.enqueue(10)
obj.dequeue()
obj.dequeue()
obj.dequeue()
print(obj.queues)
print(obj.front)
print(obj.rear)
