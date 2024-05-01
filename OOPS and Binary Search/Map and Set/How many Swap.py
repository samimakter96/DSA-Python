"""
You are maintaining a register of students roll numbers which is a array the roll numbers can be in sorted or unsorted
manner. The task is to arrange all the roll numbers in ascending order , Find the number of changes required to do so
that number should be minimum

Example 1:
Input:
nums = {2, 8, 5, 4}
Output: 1
Explanation: swap 8 with 4.

Example 2:
Input:
nums = {10, 19, 6, 3, 5}
Output: 2
Explanation: swap 10 with 3 and swap 19 with 5.
"""
# Brute Force Approach: Using Selection Sort
nums = [2, 8, 5, 4]
swap = 0
for i in range(len(nums)):
    minimum = i
    for j in range(i+1, len(nums)):
        if nums[j] < nums[minimum]:
            minimum = j
    if minimum != i:
        temp = nums[i]
        nums[i] = nums[minimum]
        nums[minimum] = temp
        swap += 1
print(swap)
# Time Complexity: O(n^2)
# Space Complexity: O(1)


# Optimal Approach: Using Hash map / Dictionary
arr = [10, 19, 6, 5, 3]
# sort the array
sorted_arr = sorted(arr)
# Create a HashMap to store the correct index of each element
index_map = {}
for i in range(len(sorted_arr)):
    num = sorted_arr[i]
    index_map[num] = i

# cyclic sort algorithm
swap = 0
for i in range(len(arr)):
    while arr[i] != sorted_arr[i]:
        correct_index = index_map[arr[i]]
        temp = arr[i]
        arr[i] = arr[correct_index]
        arr[correct_index] = temp
        swap += 1
print(swap)
# Time Complexity: O(N)  Space Complexity: O(1)


