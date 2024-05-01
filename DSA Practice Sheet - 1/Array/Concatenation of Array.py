"""
Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i]
and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
Specifically, ans is the concatenation of two nums arrays.
Return the array ans.

Example 1:

Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]
"""

nums = [1, 2, 1]
ans = []
for i in nums:
    ans.append(i)
for j in nums:
    ans.append(j)
print(ans)

# Time Complexity: O(2N)  Space Complexity: O(N)

nums = [1, 2, 3, 4]
ans = []
for i in range(2):
    for n in nums:
        ans.append(n)
print(ans)

# Time Complexity: O(2N) ---> drop constant o(N)
# Space Complexity: O(N)

# Best Solution
nums = [1, 2, 1]
n = len(nums)
for i in range(n):
    nums.append(nums[i])
print(nums)

# Time Complexity: O(N)  Space Complexity: O(1)
