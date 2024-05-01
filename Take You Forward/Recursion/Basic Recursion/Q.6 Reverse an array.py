# arr = [5, 6, 7, 8, 3]
# left = 0
# right = len(arr) - 1
#
# while left <= right:
#     arr[left], arr[right] = arr[right], arr[left]
#     left += 1
#     right -= 1
# print(arr)

# Time Complexity: O(N)  Space Complexity: O(1)


# Approach 2: Using Recursion

def reverse_array(arr, start, end):
    if start < end:
        arr[start], arr[end] = arr[end], arr[start]
        reverse_array(arr, start + 1, end - 1)


arr = [5, 6, 7, 8, 3]
start_index = 0
end_index = len(arr) - 1

reverse_array(arr, start_index, end_index)
print(arr)
