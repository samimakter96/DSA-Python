"""
Given an array integer and target value. return the index of elements whose absolute difference is equal to target

Absolute value of -9 is 9
"""

arr = [9, 5, 1, 11, 14]
target = 2

for i in range(len(arr)):
    for j in range(1, len(arr)):
        if abs(arr[i] - arr[j]) == target:
            print(i, j)

# Time Complexity: O(N^2)      Space Complexity: O(1)

# Optimal Approach:
nums = [9, 5, 1, 11, 14]
target = 2
num_map = {}
n = len(nums)
for i in range(n):
    complement = nums[i] - target
    if complement in num_map:
        # if complement in num_map dict return complement index, and the current index i
        print(num_map[complement], i)
    # if not found, add the current nums and its index i to the num_map dictionary
    num_map[nums[i]] = i

# Time Complexity: O(N)     Space Complexity: O(N)


"""
Given an integer array, return the maximum difference between any 2 adjacent elements.

input: [10, 8, 6, 4, 2]
output: 2
Explanation: the maximum of the all is 2
"""

arr = [10, 8, 6, 4, 2]
maxi = 0
for i in range(1, len(arr)):
    diff = abs(arr[i] - arr[i-1])
    if diff > maxi:
        maxi = diff
print(maxi)


