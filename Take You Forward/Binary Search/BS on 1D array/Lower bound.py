"""
Input: ‘arr’ = [1, 2, 2, 3] and 'x' = 0

Output: 0

Explanation: Index '0' is the smallest index such that 'arr[0]' is not less than 'x'
"""

# Time Complexity: O(log n)

# Given array 'arr' and a target value 'x'
arr = [1, 2, 2, 3, 5]
n = 6
x = 0

# Initialize variables for binary search
low = 0
high = n - 1

# Initialize 'ans' to the length of the array
ans = n

# Perform binary search
while low <= high:
    # Calculate the middle index
    mid = (low + high) // 2

    # Check if the middle element is greater than or equal to 'x'
    if arr[mid] >= x:
        # Update 'ans' and search in the left half
        ans = mid
        high = mid - 1
    else:
        # Search in the right half
        low = mid + 1

# Print the final result
print(ans)
