"""Creating Queue using python List - no size limit (Operations isEmpty, enqueue, dequeue, peek, delete)"""


class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        values = [str(x) for x in self.items]
        return " ".join(values)

    def is_empty(self):
        if self.items == []:
            return True
        else:
            return False

    # add element from the end of the list

    def enqueue(self, value):
        self.items.append(value)
        return "The element is inserted at the end of Queue"

    # dequeue method delete element from first because it's follow FIFO method - First In First Out
    def dequeue(self):
        if self.is_empty():
            return "There is not any element is the Queue"
        else:
            return self.items.pop(0)

    # peek method return first element
    def peek(self):
        if self.is_empty():
            return "There is not any element is the Queue"
        else:
            return self.items[0]

    def delete(self):
        self.items = None


custom_queue = Queue()
print(custom_queue.is_empty())
custom_queue.enqueue(1)
custom_queue.enqueue(2)
custom_queue.enqueue(3)
custom_queue.enqueue(4)
print(custom_queue.peek())
print(custom_queue)

