"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4
"""

# Brute Force Approach:

arr = [2, 2, 1]
# Run a loop for selecting elements
for i in range(len(arr)):
    num = arr[i]    # selected element
    count = 0
    # Find the occurrence using linear search:
    for j in range(len(arr)):
        if arr[j] == num:
            count += 1
    # If the occurrence is 1, return the number:
    if count == 1:
        print(num)

# Time Complexity: O(N^2)    Space Complexity: O(1)


# Better Approach: Using Dictionary

arr = [4, 1, 2, 1, 2]
freq_map = {}
for item in arr:
    if item in freq_map:
        freq_map[item] += 1
    else:
        freq_map[item] = 1

for key, value in freq_map.items():
    if value == 1:
        print(key)

# Better Solution: Using hashmap / dictionary
arr = [4, 1, 2, 1, 2]

num_dic = {}
for num in arr:
    num_dic[num] = num_dic.get(num, 0) + 1
# num_dic.get(num, 0) -- >  If the key is not present in num_dic, it returns the default value 0.
# num_dic.get(num, 0) + 1 --> 1. If the key num is already in the num_dic, it increments its value by 1.
# 2. If the key num is not in the num_dic, it adds a new key-value pair with num as the key and the initial value of 1.

for num, count in num_dic.items():
    if count == 1:
        print(num)
# Time Complexity: O(N) + O(M)  where N = size of the array, M = size of the dictionary
# Space Complexity: O(M)


# Optimal Solution:
arr = [4, 1, 2, 1, 2]
# XOR of two same number is always 0  i,e --> 1 ^ 1 = 0, 2 ^ 2 = 0
# XOR of a number with 0 will result in the number itself i.e --> 0 ^ 4 = 4

xor = 0
for num in arr:
    xor = xor ^ num
print(xor)

# Time Complexity: O(N)   Space Complexity: O(1)