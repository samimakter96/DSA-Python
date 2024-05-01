"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""

# Brute Force Approach:
nums = [2, 7, 11, 15]
target = 9
for i in range(len(nums)):
    for j in range(1, len(nums)):
        if nums[i] + nums[j] == target:
            print(i, j)

# Time Complexity: O(N^2)  Space Complexity: O(1)


# Better Approach / Optimal Approach: Using Dictionary
nums = [2, 7, 11, 15]
target = 9
freq_map = {}
for i in range(len(nums)):
    complement = target - nums[i]
    if complement in freq_map:
        print(freq_map[complement], i)
    else:
        freq_map[nums[i]] = i

# Time Complexity: O(N)   Space Complexity: O(N)


