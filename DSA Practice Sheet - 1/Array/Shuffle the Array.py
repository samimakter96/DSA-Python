"""
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].

Example 1:
Input: nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7]
Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].
"""

nums = [2, 5, 1, 3, 4, 7]
n = 3
result = []
for i in range(n):
    result.append(nums[i])
    result.append(nums[i+n])
print(result)

# Time Complexity: O(N)   Space Complexity: O(N)

# Approach 2: Using two pointers

nums = [2, 5, 1, 3, 4, 7]
res = []
n = 3
x = 0
y = n

while x < n:
    res.append(nums[x])
    res.append(nums[y])
    x += 1
    y += 1
print(res)