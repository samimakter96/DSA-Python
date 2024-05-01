"""Creating Stack Using List without limit"""


class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)

    # check if it is Empty
    def is_empty(self):
        if self.list == []:
            return True
        else:
            return False

    # push method
    def push(self, value):
        self.list.append(value)
        return "The element has been successfully inserted"

    # pop method
    def pop(self):
        if self.is_empty():
            return "There is not any element in the stack"
        else:
            return self.list.pop()

    # peek method
    def peek(self):
        if self.is_empty():
            return "There is not any element in the stack"
        else:
            return self.list[len(self.list) - 1]

    # delete method
    def delete(self):
        self.list = None


customs_stack = Stack()
customs_stack.push(1)
customs_stack.push(2)
customs_stack.push(3)
customs_stack.push(4)
# print(customs_stack)
# print(customs_stack.pop()
print(customs_stack.peek())
print(customs_stack)