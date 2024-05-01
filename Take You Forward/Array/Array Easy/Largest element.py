"""
Find the largest element in an array
"""

# Brute Force Approach:
arr = [1, 2, 5, 6, 7, 4, 3]
n = len(arr)
arr.sort()
largest = arr[n-1]
print("largest element in the array:", largest)


# Optimal Approach:
arr = [1, 5, 6, 3, 7, 4]
max_arr = arr[0]    # initialize first element to be maximum element
for i in range(len(arr)):
    if arr[i] > max_arr:
        max_arr = arr[i]
print("largest element in the array:", max_arr)