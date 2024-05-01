"""Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
Implement the MinStack class:"""


class MinStack:
    def __init__(self):
        # Main stack to store the actual values
        self.stack = []

        # Stack to keep track of the minimum values encountered so far
        self.min_stack = []

    def push(self, val):
        # Push the value onto the main stack
        self.stack.append(val)

        # If min_stack is not empty, compare the current value with the top of min_stack
        # Choose the minimum of the two and push it onto min_stack
        if self.min_stack:
            val = min(self.min_stack[-1], val)
        self.min_stack.append(val)

    def pop(self):
        # Pop the top element from both the main stack and min_stack
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        # Return the top element of the main stack without removing it
        return self.stack[-1]

    def get_min(self):
        # Return the top element of min_stack, representing the minimum element in the stack
        return self.min_stack[-1]


# Example usage:
obj = MinStack()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(5)
print(obj.top())  # Output: 5
print(obj.get_min())  # Output: 1
