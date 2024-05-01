"""
Given an array of integers nums and an integer k, return the total number of sub-arrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

Input: nums = [3, 1, 2, 4], k = 6
Output: 2
Explanation: The sub-arrays that sum up to 6 are [3, 1, 2] and [2, 4].
"""

# Brute Force Approach:
nums = [3, 1, 2, 4]
k = 6
count = 0
for i in range(len(nums)):
    sum_subarray = 0
    for j in range(i, len(nums)):
        sum_subarray += nums[j]
        if sum_subarray == k:
            count += 1
print(count)

# Time Complexity: O(N^2)   Space Complexity: O(1)


# Optimal Solution: Using Dictionary

# Given list of numbers
nums = [3, 1, 2, 4]

# Target sum
k = 3

# Dictionary to store prefix sums and their occurrences
mp = {0: 1}

# Variable to store the final result
ans = 0

# Variable to store the running prefix sum
pref_sum = 0

# Loop through each element in the list
for i in range(len(nums)):
    # Add the current number to the running prefix sum
    pref_sum += nums[i]

    # Check if there exists a subarray with sum equal to k
    # by subtracting k from the current prefix sum and checking
    # if the result is in the dictionary
    if pref_sum - k in mp:
        ans = ans + mp[pref_sum - k]

    # Update the dictionary with the current prefix sum
    if pref_sum not in mp:
        mp[pref_sum] = 1
    else:
        mp[pref_sum] += 1

# Print the final result
print(ans)

# Time Complexity: O(N log N)   Space complexity: O(N)

