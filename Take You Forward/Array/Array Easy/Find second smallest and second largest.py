"""
Find second smallest and second-largest element in the array
"""

# Brute Force Approach: this approach only work if there are no duplicates element in the array

arr = [1, 3, 5, 7, 2, 6]
n = len(arr)
arr.sort()

second_small = arr[1]
second_large = arr[n-2]
print(second_small)
print(second_large)


# Better Approach:

arr = [1, 3, 4, 2, 7, 7, 5]
small = float('inf')        # initialize positive infinity ---> represent the largest possible value
second_smallest = float('inf')

large = float('-inf')       # initialize negative infinity ---> represent the smallest possible value
second_largest = float('-inf')

for i in range(len(arr)):
    small = min(small, arr[i])
    large = max(large, arr[i])

for i in range(len(arr)):
    if arr[i] < second_smallest and arr[i] != small:
        second_smallest = arr[i]

    if arr[i] > second_largest and arr[i] != large:
        second_largest = arr[i]

print("Second Smallest:", second_smallest)
print("Second Largest:", second_largest)


# Optimal Approach (Best Solution):

arr = [1, 3, 4, 2, 7, 7, 5]

small = float('inf')
second_small = float('inf')

large = float('-inf')
second_large = float('-inf')

for num in arr:
    if num < small:
        second_small = small
        small = num
    elif num < second_small and num != small:
        second_small = num

    if num > large:
        second_large = large
        large = num
    elif num > second_large and num != large:
        second_large = num

print("Second Smallest element:", second_small)
print("Second Largest element:", second_large)