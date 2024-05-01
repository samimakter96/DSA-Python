# Types of Operation:
"""
1. Push --> insert element to the first  / if it is full you won't able to push
2. Pop  --> remove element from the last / if it is empty you won't able to pop
3. Peek --> it tell you top most element inside the stack
4. IsEmpty --> if my top most element is -1 that means it is empty
5. Full ---> check it is full or not
"""


class Stack:
    def __init__(self):
        self.top = -1
        self.stack = []

    def push(self, element):
        self.top = self.top + 1
        self.stack.append(element)

    def pop(self):
        self.stack.pop()
        self.top = self.top-1

    def peek(self):
        return self.stack[self.top]

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False


x = Stack()
print(x.isEmpty())
x.push(1)
x.push(3)
x.push(5)
x.push(8)
x.pop()
print(x.stack)
print(x.peek())
print(x.isEmpty())
#
#
# # Inbuilt Method:
#
# x = []
# x.append(1)
# x.append(5)
# x.append(7)
# print(x)
# # x.pop()     # remove top most element / last element of the stack
# print(x[len(x)-1])  # it will give me the top most element / last element
# print(x)

# if len(x) == 0:   # it check the stack is empty or not
#     print("Empty")
# else:
#     print("Not Empty")
# print(x)
# print(not stack)   # it means the stack is empty


class Stack:

    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        self.stack.pop()

    def is_empty(self):
        if len(self.stack) == 0:
            print("the stack is empty")
        else:
            print("the stack is not empty")

    def top(self):
        return self.stack[-1]


x = Stack()
x.is_empty()
x.push(1)
x.push(2)
x.push(3)
x.push(4)
x.push(5)
print(x.stack)
print(x.top())
x.is_empty()
x.pop()
x.pop()
print(x.stack)