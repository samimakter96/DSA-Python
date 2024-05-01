"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element
always exists in the array.

Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""

# Brute Force Approach:
# nums = [2, 2, 1, 1, 1, 2, 2]
#
# n = len(nums)
# for i in range(n):
#     count = 0
#     for j in range(n):
#         if nums[j] == nums[i]:
#             count = count + 1
#
#     if count > (n // 2):
#         print(nums[i])

# Time Complexity: O(N^2)   Space Complexity: O(1)


# Better Approach: Using Dictionary

# nums = [2, 2, 1, 1, 1, 2, 2, 1, 1]
# n = len(nums)
# my_map = {}
# for i in nums:
#     if i in my_map:
#         my_map[i] += 1
#     else:
#         my_map[i] = 1
#
# for key, value in my_map.items():
#     if value > (n // 2):
#         print(key)

# Time Complexity: O(NlogN) + O(N)   Space Complexity: O(N)


# Optimal Approach: Moore’s Voting Algorithm


def majority_element(nums):
    n = len(nums)
    count = 0
    element = None

    # Find the majority element
    for i in range(n):
        if count == 0:
            count = 1
            element = nums[i]
        elif element == nums[i]:
            count = count + 1
        else:
            count = count - 1

    # Count occurrences of the majority element
    count1 = 0
    for i in range(n):
        if nums[i] == element:
            count1 = count1 + 1

    # Check if the majority element occurs more than half the array size
    if count1 > (n / 2):
        return element
    return -1


arr = [2, 2, 1, 1, 1, 2, 2]
print(majority_element(arr))

# Time Complexity: O(N)   Space Complexity: O(1)

# We can solve this way also
nums = [2, 2, 1, 1, 1, 2, 2, 1, 1]
count = 0
element = 0

for num in nums:
    if count == 0:
        element = num

    elif num == element:
        count = count + 1
    else:
        count = count - 1
print(element)