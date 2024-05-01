"""
Given an array, and an element num the task is to find if num is present in the given array or not.
If present print the index of the element or print -1.

Example 1:
Input: arr[]= 1 2 3 4 5, num = 3
Output: 2
Explanation: 3 is present in the 2nd index
"""


def linear_search(arr, target):

    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


nums = [1, 2, 3, 4, 5]
tar = 3
print(linear_search(nums, tar))