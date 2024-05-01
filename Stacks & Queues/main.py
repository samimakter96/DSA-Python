class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        values = [str(x) for x in self.items]
        return " ".join(values)

    def is_empty(self):
        if len(self.items) == 0:
            return "The queue is empty"
        else:
            return False

    def enqueue(self, val):
        self.items.append(val)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return "The queue is empty, it can not dequeue"

    def get_first_element(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return "the queue is empty, it can not have first element"


my_queue = Queue()
print(my_queue.is_empty())
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)

print(my_queue)
print(my_queue.dequeue())
print(my_queue)
print(my_queue.get_first_element())
