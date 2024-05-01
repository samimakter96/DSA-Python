"""
Check if an array is sorted. if sorted return True if not return False
"""

# Brute Fore Approach:


def is_sorted(arr):

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                return False
    return True


nums = [1, 2, 4, 3, 5, 7, 6]
print(is_sorted(nums))

# Time Complexity: O(N^2)   Space Complexity: O(1)

# Optimal Approach (Best Approach):


def is_arr_sort(arr, n):

    for i in range(1, n):
        if arr[i] < arr[i-1]:
            return False
    return True


nums = [1, 2, 3, 4, 5, 6]
n = len(nums)
print(is_arr_sort(nums, n))

# Time Complexity: O(N)   Space Complexity: O(1)
