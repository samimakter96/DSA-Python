# Given sorted array 'arr' and target value 'target'
arr = [1, 2, 4, 7]
n = len(arr)
target = 6

# Initialize 'ans' to the length of the array
ans = n

# Initialize variables for binary search
low = 0
high = len(arr) - 1

# Perform binary search
while low <= high:
    # Calculate the middle index
    mid = (low + high) // 2

    # Check if the middle element is greater than or equal to 'target'
    if arr[mid] >= target:
        # Update 'ans' and search in the left half
        ans = mid
        high = mid - 1
    else:
        # Search in the right half
        low = mid + 1

# Print the final result
print(ans)
