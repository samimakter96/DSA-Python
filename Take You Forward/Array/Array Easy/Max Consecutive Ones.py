"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3

Example 2:
Input: nums = [1,0,1,1,0,1]
Output: 2
"""

nums = [1, 1, 0, 1, 1, 1]
count = 0
maximum = 0
for i in range(len(nums)):
    if nums[i] == 1:
        count += 1
    else:
        count = 0

    if count > maximum:
        maximum = count
print(maximum)

# Time Complexity: O(N)  Space Complexity: O(1)

