# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
"""
Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]

Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
"""

"""Try to Solve in time Complexity 0(n*k)."""

nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
k = k % len(nums)
for i in range(k):
    temp = nums[len(nums)-1]
    for j in range(len(nums)-2, -1, -1):
        nums[j+1] = nums[j]
    nums[0] = temp
print(nums)

# Approach: 2
arr = [1, 2, 3, 4, 5, 6, 7]
print("Original array before right shifting:", arr)
k = 3
k = k % len(arr)
for count in range(k):
    temp = arr[-1]
    for i in range(len(arr)-1, -1, -1):
        arr[i] = arr[i-1]
    arr[0] = temp
print("array after right shifting:", arr)

""" Time Complexity: O(n^2) """


""" Left Shift """
a = [5, 10, 15, 20, 25]
print("List before shifting:", a)
n = 2
n = n % len(a)
for count in range(n):
    temp = a[0]
    for i in range(1, len(a)):
        a[i-1] = a[i]
    a[len(a)-1] = temp
print("List after left shifting:", a)


# Approach: 2
arr = [1, 2, 3, 4, 5, 6, 7]
print("Original array:", arr)
k = 3
k = k % len(arr)
for count in range(k):
    temp = arr[0]
    for i in range(len(arr)-1):
        arr[i] = arr[i+1]
    arr[-1] = temp
print("array after left shift:", arr)
