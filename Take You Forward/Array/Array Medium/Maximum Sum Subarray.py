"""
Given an integer array nums, find the subarray with the largest sum, and return its sum.
"""

# Brute Force Approach:
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_subarray = 0
for i in range(len(nums)):
    for j in range(i, len(nums)):
        sum_subarray = 0
        for k in range(i, j+1):
            sum_subarray += nums[k]
            if sum_subarray > max_subarray:
                max_subarray = sum_subarray

print(max_subarray)

# Time Complexity: O(N^3)   Space Complexity: O(1)


# Better Approach:
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_subarray = 0
for i in range(len(nums)):
    sum_subarray = 0
    for j in range(i, len(nums)):
        sum_subarray += nums[j]
        if sum_subarray > max_subarray:
            max_subarray = sum_subarray

print(max_subarray)

# Time Complexity: O(N^2)   Space Complexity: O(1)


# Optimal Approach: Using Kadane,s Algorithm
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

maxi = float('-inf')
sum_subarray = 0

for i in range(len(arr)):
    sum_subarray += arr[i]

    if sum_subarray > maxi:
        maxi = sum_subarray

    # If sum < 0: discard the sum calculated
    if sum_subarray < 0:
        sum_subarray = 0

    # To consider the sum of the empty subarray

    # if maxi < 0: maxi = 0

print(maxi)

# Time Complexity: O(N)   Space Complexity: O(1)

# Follow up Question: Printing the maximum sum subarray
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

max_sum = float('-inf')
current_sum = 0
start_index = 0
end_index = 0
temp_start_index = 0

for i in range(len(arr)):
    current_sum += arr[i]

    if current_sum > max_sum:
        max_sum = current_sum

        start_index = temp_start_index
        end_index = i

    if current_sum < 0:
        current_sum = 0
        temp_start_index = i + 1

# Print the maximum sum and the corresponding subarray
print(f"Maximum sum: {max_sum}")
print("Subarray:", arr[start_index:end_index + 1])
