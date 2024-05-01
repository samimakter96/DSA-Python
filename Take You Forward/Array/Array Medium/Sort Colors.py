"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color
 are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.



Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
"""

# Brute Force Approach: Using Bubble Sort (we can use any sorting algorithm)
# nums = [2, 0, 2, 1, 1, 0]
# for j in range(len(nums)-1):
#     for i in range(len(nums)-1-j):
#         if nums[i] > nums[i+1]:
#             temp = nums[i]
#             nums[i] = nums[i+1]
#             nums[i+1] = temp
# print(nums)

# Time Complexity: O(N^2)  Space Complexity: O(1)


# Better Approach:
nums = [2, 0, 2, 1, 1, 0]

count0 = 0
count1 = 0
count2 = 0
for i in range(len(nums)):
    if nums[i] == 0:
        count0 += 1
    elif nums[i] == 1:
        count1 += 1
    else:
        count2 += 1

for i in range(count0):
    nums[i] = 0
for i in range(count0, count0 + count1):
    nums[i] = 1
for i in range(count0 + count1, len(nums)):
    nums[i] = 2
print(nums)

# Time Complexity: O(2N)   Space Complexity: O(1)


# Optimal Approach: using Dutch National flag algorithm

nums = [2, 0, 2, 1, 1, 0]
low = 0
mid = 0
high = len(nums)-1

while mid <= high:
    if nums[mid] == 0:
        nums[low], nums[mid] = nums[mid], nums[low]
        low = low + 1
        mid = mid + 1

    elif nums[mid] == 1:
        mid = mid + 1
    else:
        nums[mid], nums[high] = nums[high], nums[mid]
        high = high - 1

print(nums)`