# Brute Force Approach:
nums = [3, 1, -2, -5, 2, -4]
n = len(nums)
pos = []
neg = []
for i in range(n):
    if nums[i] > 0:
        pos.append(nums[i])
    else:
        neg.append(nums[i])

for i in range(len(pos)):
    nums[2 * i] = pos[i]

for i in range(len(neg)):
    nums[2 * i+1] = neg[i]

print(nums)

# Time Complexity: O(N)   Space Complexity: O(N)

# Optimal Approach:
nums = [3, 1, -2, -5, 2, -4]
n = len(nums)
pos = 0
neg = 1
ans = [0] * n
for i in range(n):
    if nums[i] > 0:
        ans[pos] = nums[i]
        pos += 2
    else:
        ans[neg] = nums[i]
        neg += 2

print(ans)
