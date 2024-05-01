"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every
element is distinct.
Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
"""

# Brute Force Approach:
nums = [1, 2, 3, 4]
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] == nums[j]:
            print(True)
print(False)

# Time Complexity: O(N^2)   Space Complexity: O(1)

# Approach 2: Using Sorting
nums = [1, 2, 3, 1]
nums.sort()
for i in range(1, len(nums)):
    if nums[i] == nums[i-1]:
        print("True")
print(False)

# Sorting has a time complexity: O(n log n)

# Approach 3: Using Set
arr = [1, 2, 3, 2, 4, 5]
seen = set()
for item in arr:
    if item in seen:
        print(True)
    seen.add(item)
print(False)

# Time Complexity: O(N)   Space Complexity: O(N)


# Approach 4: Using Dictionary
nums = [1, 2, 3, 1]
num_map = {}

for item in nums:
    if item in num_map and num_map[item] >= 1:
        print(True)
    num_map[item] = num_map.get(item, 0) + 1
print(False)

# Time Complexity: O(N)  Space Complexity: O(N)
