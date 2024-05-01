class Queues:

    def __init__(self):
        self.queues = []

    def __str__(self):
        values = [str(x) for x in self.items]
        return " ".join(values)

    def is_empty(self):
        return len(self.queues) == 0

    def enqueue(self, element):
        self.queues.append(element)

    def dequeue(self):
        if not self.is_empty():
            return self.queues.pop(0)
        else:
            print("Queue is empty, cannot dequeue")

    def get_first_element(self):
        if not self.is_empty():
            return self.queues[0]
        else:
            print("Queue is empty, no element at the front")


my_queue = Queues()
print(my_queue.is_empty())
my_queue.enqueue(5)
my_queue.enqueue(10)
my_queue.enqueue(7)
my_queue.enqueue(3)
print(my_queue.queues)
print(my_queue.get_first_element())
my_queue.dequeue()
my_queue.dequeue()
my_queue.dequeue()
my_queue.dequeue()
print(my_queue.queues)