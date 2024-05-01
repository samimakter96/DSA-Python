class MyCircularQueue:

    def __init__(self, k: int):
        # Initialize the circular queue with given capacity 'k'
        self.head = 0  # Initialize the head pointer to 0
        self.tail = 0  # Initialize the tail pointer to 0
        self.size = 0  # Initialize the current size to 0
        self.k = k  # Set the capacity of the circular queue
        self.q = [None] * k  # Create an array 'q' of size 'k' to store the elements

    def enQueue(self, value: int) -> bool:
        # Add an element to the circular queue
        if self.isFull():  # Check if the queue is full
            return False
        self.q[self.tail] = value  # Add the value to the tail position
        self.size += 1  # Increase the size of the queue
        self.tail = (self.tail + 1) % self.k  # Update the tail pointer in a circular manner
        return True

    def deQueue(self) -> bool:
        # Remove an element from the circular queue
        if self.isEmpty():  # Check if the queue is empty
            return False
        self.size -= 1  # Decrease the size of the queue
        self.head = (self.head + 1) % self.k  # Update the head pointer in a circular manner
        return True

    def Front(self) -> int:
        # Get the front element of the circular queue
        if self.isEmpty():  # Check if the queue is empty
            return -1
        return self.q[self.head]  # Return the element at the head position

    def Rear(self) -> int:
        # Get the rear element of the circular queue
        if self.isEmpty():  # Check if the queue is empty
            return -1
        return self.q[self.tail - 1]  # Return the element at the position before the tail

    def isEmpty(self) -> bool:
        # Check if the circular queue is empty
        if self.size == 0:
            return True
        return False

    def isFull(self) -> bool:
        # Check if the circular queue is full
        if self.size == self.k:
            return True
        return False
