""" Given an integer array nums, rotate the array to the right by k steps, where k is non-negative."""
# Try to Solve in time Complexity 0(n) without any extra Space

# nums = [1, 2, 3, 4, 5, 6, 7]
# k = 3
# k = k % len(nums)
# left, right = 0, (len(nums)-1)
# while left < right:
#     nums[left], nums[right] = nums[right], nums[left]
#     left = left + 1
#     right = right - 1
#
# left, right = 0, (k-1)
# while left < right:
#     nums[left], nums[right] = nums[right], nums[left]
#     left = left + 1
#     right = right - 1
#
# left, right = k, (len(nums)-1)
# while left < right:
#     nums[left], nums[right] = nums[right], nums[left]
#     left = left + 1
#     right = right - 1
#
# print(nums)

""" Time Complexity O(n) """
""" Space Complexity O(1)"""


a = [1, 2, 3, 4, 5, 6, 7]
print("original a:", a)
k = 3
k = k % len(a)
start = 0
end = len(a)-1
while start < end:
    a[start], a[end] = a[end], a[start]
    start += 1
    end -= 1
print("reverse the entire array:", a)
start = 0
end = k-1
while start < end:
    a[start], a[end] = a[end], a[start]
    start += 1
    end -= 1
print("reverse start to k:", a)
start = k
end = len(a)-1
while start < end:
    a[start], a[end] = a[end], a[start]
    start += 1
    end -= 1
print("reverse k to end:", a)


""" LEFT SHIFT """

arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
print("Original Array:", arr)
k = k % len(arr)

st = 0
end = len(arr)-1
while st < end:
    arr[st], arr[end] = arr[end], arr[st]
    st += 1
    end -= 1
print("Reverse the entire array:", arr)

st = 0
end = len(arr) - k - 1  # end = k
while st < end:
    arr[st], arr[end] = arr[end], arr[st]
    st += 1
    end -= 1
print("Reverse the array from 0 to 3:", arr)

st = len(arr) - k
end = len(arr) - 1
while st < end:
    arr[st], arr[end] = arr[end], arr[st]
    st += 1
    end -= 1
print("Reverse the array from 4 to end:", arr)
