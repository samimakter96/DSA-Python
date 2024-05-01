from collections import deque

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
# Initialize an empty list to store the maximum elements in each window
output = []

# Initialize a deque to store indices of elements, and two pointers for the sliding window
q = deque()
left = 0
right = 0

# Main loop that iterates through the array 'nums'
while right < len(nums):

    # Pop smaller values from the back of the deque until finding an equal or larger element
    while q and nums[q[-1]] < nums[right]:
        q.pop()

    # Append the current index to the deque
    q.append(right)

    # Check if the left pointer has moved past the front element in the deque
    if left > q[0]:
        q.popleft()

    # Check if the window size has been reached or surpassed
    if (right + 1) >= k:
        # Append the maximum element in the current window to the 'output' list
        output.append(nums[q[0]])
        # Move the left pointer to slide the window
        left += 1

    # Move the right pointer to expand the window
    right += 1

# Return the list containing the maximum elements in each window
print(output)
