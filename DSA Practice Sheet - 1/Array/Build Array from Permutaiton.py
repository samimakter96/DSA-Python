"""
Input: nums = [0,2,1,5,3,4]
Output: [0,1,2,4,5,3]
Explanation: The array ans is built as follows:
ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
    = [nums[0], nums[2], nums[1], nums[5], nums[3], nums[4]]
    = [0,1,2,4,5,3]
"""

# Brute Force Approach

nums = [0, 2, 1, 5, 3, 4]
n = len(nums)
ans = [0] * n
for i in range(len(nums)):
    ans[i] = nums[nums[i]]
print(ans)

# TC: O(N)  SC: O(N)


# Optimal Solution:
nums = [0, 2, 1, 5, 3, 4]
n = len(nums)

for i, num in enumerate(nums):
    nums[i] = nums[i] + n * (nums[num] % n)

for i in range(n):
    nums[i] //= n
print(nums)

# TC: O(N)  SC: O(1)
