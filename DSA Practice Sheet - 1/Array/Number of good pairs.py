"""
Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
"""
# Brute Force Approach:
nums = [1, 2, 3, 1, 1, 3]
count = 0
for i in range(len(nums)):
    for j in range(1, len(nums)):
        if nums[i] == nums[j] and i < j:
            count += 1
print(count)

# Time Complexity: O(N^2)   Space Complexity: O(1)


# Better Approach: Using Dictionary
nums = [1, 2, 3, 1, 1, 3]

# Create an empty dictionary to store the frequency of each number
freq_map = {}

# Initialize a variable to count the pairs
count_pair = 0

# Loop through each item in the list 'nums'
for item in nums:
    # Increment the count_pair by the current frequency of the item in freq_map
    count_pair += freq_map.get(item, 0)

    # Update the frequency of the current item in freq_map
    freq_map[item] = freq_map.get(item, 0) + 1

# Print the total count of pairs
print(count_pair)


# Time Complexity: O(N)   Space Complexity: O(N)
