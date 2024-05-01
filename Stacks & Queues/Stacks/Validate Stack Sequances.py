"""
Given two integer arrays pushed and popped each with distinct values, return true if this could have been the result of
a sequence of push and pop operations on an initially empty stack, or false otherwise.

Example 1:
Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4),
pop() -> 4,
push(5),
pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

Example 2:
Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2.

"""

pushed = [1, 2, 3, 4, 5]
popped = [4, 5, 3, 2, 1]

stack = []
j = 0
# iterate through the pushed element
for x in pushed:
    # append the element into the stack
    stack.append(x)
    # while stack is non-empty and popped[j] == stack[-1]
    # if popped[0] element is == stack[-1] last element then we have to pop() the element and increase popped[j] for the
    # next comparison
    while stack and popped[j] == stack[-1]:
        stack.pop()
        j = j + 1

# after popping all the element if stack is still: it means it's a validate sequences
if len(stack) == 0:
    print(True)
else:
    print(False)
