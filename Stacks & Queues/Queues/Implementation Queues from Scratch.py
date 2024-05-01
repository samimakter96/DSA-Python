class Queue:
    def __init__(self):
        self.items = []

    # for printing
    def __str__(self):
        values = [str(x) for x in self.items]
        return " ".join(values)

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Queue is empty. Cannot dequeue.")

    def get_first_element(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print("Queue is empty. No elements at the front.")


# Create a Queue
my_queue = Queue()

# Enqueue elements
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)

# Check if the queue is empty
print("Is the queue empty?", my_queue.is_empty())

# Get the first element
print("Element at the front:", my_queue.get_first_element())

# Dequeue elements
print("Dequeued element:", my_queue.dequeue())
print("Dequeued element:", my_queue.dequeue())

# Check if the queue is empty after de-queuing
print("Is the queue empty now?", my_queue.is_empty())
