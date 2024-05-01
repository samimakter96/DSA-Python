"""In A exam with negative marking the passing criteria is you have to score zero or positive marks .
we have given an array which denotes the score of the students in that exam .
you have to move all the failed students to last of the array ."""

# arr[] = {1, -1, 3, 2, -7, -5, 11, 6 }
# Output :  1 3 2 11 6 -1 -7 -5

# arr = [-5, 7, -3, -4, 9, 10, -1, 11]
# negative_value = []
# for element in arr:
#     if element < 0:
#         negative_value.append(element)
# result = [x for x in arr if x >= 0] + negative_value
# print(result)


# def move_negative_to_end(arr):
#     negative_value = []
#     for element in arr:
#         if element < 0:
#             negative_value.append(element)
#
#     result = [x for x in arr if x >= 0] + negative_value
#     return result
#
#
# arr = [1, -1, 3, 2, -7, -5, 11, 6]
# result_array = move_negative_to_end(arr)
# print(result_array)


arr = [1, -1, 3, 2, -7, -5, 11, 6]
num = []
neg_num = []
for i in arr:
    if i > 0:
        num.append(i)
    else:
        neg_num.append(i)
print(num + neg_num)


# Optimal Approach: Using two pointers
def move_failed_students(arr):
    # Initialize two pointers
    left = 0
    right = len(arr) - 1

    # Iterate through the array
    while left < right:
        # Check if the element at the left pointer is negative
        if arr[left] < 0:
            # Swap the elements at the left and right pointers
            arr[left], arr[right] = arr[right], arr[left]
            # Move the right pointer one step to the left
            right -= 1
        else:
            # Move the left pointer one step to the right
            left += 1


# Example usage
arr = [1, -1, 3, 2, -7, -5, 11, 6]
move_failed_students(arr)

# Print the modified array
print(arr)

# Time Complexity: O(N)   Space Complexity: O(1)
