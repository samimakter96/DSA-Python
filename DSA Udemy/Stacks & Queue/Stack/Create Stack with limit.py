"""Create stack using list with limit"""


class Stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)

    # is Empty
    def is_empty(self):
        if len(self.list) == 0:
            return True
        else:
            return False

    # is Full
    def is_full(self):
        if len(self.list) == self.max_size:
            return True
        else:
            return False

    # push method
    def push(self, value):
        if self.is_full():
            return "The stack is full"
        else:
            self.list.append(value)
            return "The element has been successfully inserted"

    # pop method
    def pop(self, value):
        if self.is_empty():
            return "There is not any element in the stack"
        else:
            return self.list.pop()

    # peek method
    def peek(self):
        if self.is_empty():
            return "There is not any element in the stack"
        else:
            return self.list[len(self.list)-1]

    # delete method
    def delete(self):
        self.list = None


custom_stack = Stack(4)
print(custom_stack.is_empty())
print(custom_stack.is_full())
custom_stack.push(1)
custom_stack.push(2)
custom_stack.push(3)
print(custom_stack)
