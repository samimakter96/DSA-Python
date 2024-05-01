"""
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each
nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.

Example 1:
Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
"""

# Brute Force Approach:
nums = [8, 1, 2, 2, 3]

ans = []
for i in range(len(nums)):
    count = 0
    for j in range(1, len(nums)):
        if j != i and nums[j] < nums[i]:
            count += 1
    ans.append(count)

print(ans)

# Time Complexity: O(N^2)   Space Complexity: O(N)

# Better Solution:
nums = [8, 1, 2, 2, 3]

sort_nums = sorted(nums)

ans = []
for i in nums:
    ans.append(sort_nums.index(i))
print(ans)

# Time Complexity: O(N log N)   Space Complexity: O(N)

nums = [8, 1, 2, 2, 3]

sort_nums = sorted(nums)
num_map = {}
result = []
for i in range(len(sort_nums)):
    if sort_nums[i] not in num_map:
        num_map[sort_nums[i]] = i

for i in nums:
    result.append(num_map[i])
print(result)