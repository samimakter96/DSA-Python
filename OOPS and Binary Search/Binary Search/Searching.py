"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search
target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
"""


def searching(nums, target):

    st = 0
    end = len(nums)-1

    while st <= end:
        mid = (st + end) // 2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            end = mid - 1
        else:
            st = st + 1

    return -1


num = [-1, 0, 3, 5, 9, 12]
tar = 9
print(searching(num, tar))