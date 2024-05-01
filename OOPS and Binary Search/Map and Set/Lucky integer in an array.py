"""
Given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value.
Return the largest lucky integer in the array. If there is no lucky integer return -1.

Example 1:
Input: arr = [2,2,3,4]
Output: 2
Explanation: The only lucky number in the array is 2 because frequency[2] == 2.
"""

# Brute Force Approach:

nums = [2, 2, 3, 4]
max_luck_integer = -1
for i in nums:
    if nums.count(i) == i:
        max_freq = i
        if max_freq > max_luck_integer:
            max_luck_integer = max_freq
print(max_luck_integer)

# Time Complexity : O(N^2)  Space Complexity: O(1)


# Optimal Solution: Using hashmap / dictionary
# Given list
arr = [2, 2, 3, 4]

# Create an empty hashmap to store the frequency of each element
frequency_map = {}

# Step 1: Populate the hashmap with the frequency of each element
for num in arr:
    if num in frequency_map:
        frequency_map[num] += 1   # we check if it's already in the frequency_map. If yes, we increment its frequency
    else:
        frequency_map[num] = 1    # otherwise, we set its frequency to 1.
# frequency_map after Step 1: {2: 2, 3: 1, 4: 1}

# Initialize max_num to -1
max_freq = -1

# Step 2: Find the maximum frequency and corresponding element
for key, value in frequency_map.items():
    if key == value and value > max_freq:
        max_freq = key

# max_num after Step 2: 2

# Step 3: Print the result
print(max_freq)

# Time Complexity: O(N)   Space Complexity: O(1)
