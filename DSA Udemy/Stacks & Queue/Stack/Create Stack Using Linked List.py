class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next


class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        values = [str(x.value) for x in self.LinkedList]
        return '\n'.join(values)

    def is_empty(self):
        if self.LinkedList.head == None:
            return True
        else:
            return False

    def push(self, value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node

    def pop(self):
        if self.is_empty():
            return "There is not any element in the stack"
        else:
            node_value = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return node_value

    def peek(self):
        if self.is_empty():
            return "There is not any element in the stack"
        else:
            node_value = self.LinkedList.head.value
            return node_value

    def delete(self):
        self.LinkedList.head = None


custom_stack = Stack()
custom_stack.push(1)
custom_stack.push(2)
custom_stack.push(3)
print(custom_stack)
print("-------")
# custom_stack.pop()
print(custom_stack.peek())

