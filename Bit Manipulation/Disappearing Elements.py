nums = [4, 3, 2, 7, 8, 2, 3, 1]
result = []
for i in range(1, len(nums)):
    if i not in nums:
        result.append(i)
print(result)
""" Time Complexity: O(n)   Space Complexity: O(n) """


nums = [4, 3, 2, 7, 8, 2, 3, 1]
n = len(nums)
nums = set(nums)
result = []
for i in range(1, n + 1):
    if i not in nums:
        result.append(i)
print(result)
""" Time Complexity: O(n)   Space Complexity: O(n) """


# nums = [4, 3, 2, 7, 8, 2, 3, 1]
# for i in range(len(nums)):
#     temp = abs(nums[i]) - 1
#     if nums[temp] > 0:
#         nums[temp] *= -1
#
# res = []
# for i, n in enumerate(nums):
#     if n > 0:
#         res.append(i+1)
# print(res)

a = [4, 3, 2, 7, 8, 2, 3, 1]
b = []
for i in range(0, len(a)):
    b.append(0)
# print(b)
for i in range(0, len(a)):
    correct_index = a[i]-1
    b[correct_index] = a[i]
# print(b)
ans = []
for i in range(0, len(a)):
    if b[i] == 0:
        ans.append(i+1)
print(ans)
""" Time Complexity: O(n) """
""" Space Complexity: O(n) """


arr = [4, 3, 2, 7, 8, 2, 3, 1]

# Phase 1: Rearrange elements in-place
for i in range(len(arr)):
    while arr[i] != arr[arr[i] - 1]:
        arr[arr[i] - 1], arr[i] = arr[i], arr[arr[i] - 1]

# Phase 2: Find missing values
ans = []
for i in range(len(arr)):
    if arr[i] != i + 1:
        ans.append(i + 1)
print(ans)

""" Time Complexity: O(n) """
""" Space Complexity: O(1) """


# Approach : 2

# Phase 1: Rearrange elements in-place
arr = [4, 3, 2, 7, 8, 2, 3, 1]
n = len(arr)
i = 0
x = arr[i]
# index = i

while i < n:
    correct_index = x - 1
    if arr[correct_index] == x:
        i = i + 1
        if i == n:
            break
        x = arr[i]
        continue

    temp = arr[correct_index]
    arr[correct_index] = x
    x = temp

# print(arr)

# Phase 2: Find missing values
ans = []
for i in range(1, len(arr)):
    if i not in arr:
        ans.append(i)

print(ans)

""" Time Complexity: O(n) """
""" Space Complexity: O(1) """


arr = [4, 3, 2, 7, 8, 2, 3, 1]

for i in range(len(arr)):
    while arr[i] != arr[arr[i]-1]:
        temp = arr[arr[i]-1]
        arr[arr[i]-1] = arr[i]
        arr[i] = temp

ans = []
for i in range(1, len(arr)):
    if i not in arr:
        ans.append(i)
    # if arr[i] != i + 1:
    #     ans.append(i + 1)
print(ans)
