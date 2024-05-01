nums = [1, 2, 3, 4, 3]
n = len(nums)
stack = []          # Create an empty stack to keep track of elements in the 'nums' list.
nge = [-1] * n   # Initialize an array 'nge' with -1, representing the Next Greater Element (NGE) for each element in 'nums'.

# Loop through the elements in reverse order (from last to first) twice.
for i in range(2*n-1, -1, -1):
    # While the stack is not empty and the current element is greater than or equal to the element at the top of the stack,
    # pop elements from the stack until this condition is not met.
    while stack and stack[-1] <= nums[i % n]:
        stack.pop()

    # If the current index 'i' is less than the length of 'nums', update the NGE for the corresponding element.
    if i < n:
        # If the stack is not empty, assign the top element of the stack as the NGE for the current element.
        # Otherwise, set the NGE to -1.
        if stack:
            nge[i] = stack[-1]
        else:
            nge[i] = -1

    # Push the current element to the stack.
    stack.append(nums[i % n])

# Print the array 'nge' containing the Next Greater Element for each element in 'nums'.
print(nge)
