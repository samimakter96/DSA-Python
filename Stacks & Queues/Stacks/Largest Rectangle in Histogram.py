"""
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return
the area of the largest rectangle in the histogram.

Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
"""

heights = [2, 1, 5, 6, 2, 3]
# Initialize variables
max_area = 0
stack = []  # Stack to keep track of pairs (index, height)

# Iterate through each index and height in the input 'heights'
for i, h in enumerate(heights):
    start = i  # Initialize 'start' as the current index

    # Check if the stack is not empty and the current height is smaller than the height at the top of the stack
    while stack and stack[-1][1] > h:
        # Pop the top of the stack and calculate the area using the popped index and height
        index, height = stack.pop()
        max_area = max(max_area, height * (i - index))
        start = index  # Update 'start' to the popped index

    # Push the current index and height onto the stack
    stack.append((start, h))

# Process any remaining elements in the stack
for i, h in stack:
    max_area = max(max_area, h * (len(heights) - i))

# Return the maximum area
print(max_area)
