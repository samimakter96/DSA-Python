"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""

# Brute Force Approach:
# nums = [2, 7, 11, 15]
# target = 9
#
# for i in range(len(nums)):
#     for j in range(1, len(nums)):
#         if nums[i] + nums[j] == target:
#             print(i, j)

# Time Complexity: O(N^2)   Space Complexity: O(1)

# Solution 2: (Two-pass Hash Table)
nums = [2, 7, 11, 15]
target = 9

num_dict = {}
n = len(nums)
# Build the hash table / dictionary
for i in range(n):
    num_dict[nums[i]] = i

# Find the complement
for i in range(n):
    complement = target - nums[i]
    if complement in num_dict and num_dict[complement] != i:
        print(i, num_dict[complement])

# Time Complexity : O(N)  Space Complexity: O(N)


# Solution 3: (One pass Hash Table)
nums = [2, 7, 11, 15]
target = 9

num_map = {}
n = len(nums)
for i in range(n):
    complement = target - nums[i]
    if complement in num_map:
        # if complement in num_map dict return complement index, and the current index i
        print(num_map[complement], i)
    # if not found, add the current nums and its index i to the num_map dictionary
    num_map[nums[i]] = i

# Time Complexity : O(N)  Space Complexity: O(N)
