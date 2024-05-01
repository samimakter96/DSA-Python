"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements

Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
"""

# Brute Force Approach:

arr = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]
temp = []
# Copy non-zero elements from original to temp array
for i in range(len(arr)):
    if arr[i] != 0:
        temp.append(arr[i])

# Number of non-zero elements
non_zero = len(temp)
# Copy elements from temp to fill first non_zero fields of original array
for i in range(non_zero):
    arr[i] = temp[i]
# Fill the rest of the cells with 0
for i in range(non_zero, len(arr)):
    arr[i] = 0
print(arr)

# TC --> O(2N)   SC --> O(N)


# Optimal Solution:

arr = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]
j = -1  # first we set j is -1 because we want to find out first 0
for i in range(len(arr)):
    if arr[i] == 0:
        j = i
        break
# after iterating if j is still -1 that means all are non zero element means there is no zero
if j == -1:  # edge case
    print(arr)

# if arr[i] non zero element then we swap with arr[j]
for i in range(j + 1, len(arr)):
    if arr[i] != 0:
        arr[i], arr[j] = arr[j], arr[i]
        j = j + 1
print(arr)

# TC --> O(N)   SC --> O(1)
