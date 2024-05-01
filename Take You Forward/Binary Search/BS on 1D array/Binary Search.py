"""Iterative approach"""


def binary_search(arr, target):

    low = 0
    high = len(arr)-1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1


arr = [1, 3, 7, 9, 11, 12, 45]
target = 7
print(binary_search(arr, target))


"""Recursive Implementation"""


def binary_search(nums, low, high, target):
    # Base Case: If low is greater than target, the target is not in the list
    if low > high:
        return -1

    # Calculate the mid-index of the current search space
    mid = (low + high) // 2

    # Check if the element at mid-index is equal to the target
    if nums[mid] == target:
        return mid

    # If target is greater than the element at mid-index, search the right half
    elif target > nums[mid]:
        return binary_search(nums, mid + 1, high, target)

    # If target is less than the element at mid-index, search the left half
    else:
        return binary_search(nums, low, mid - 1, target)


# Example usage:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_value = 6
result = binary_search(my_list, 0, len(my_list) - 1, target_value)

# Check if the result is found or not
if result != -1:
    print(f"Element {target_value} is present at index {result}.")
else:
    print(f"Element {target_value} is not present in the list.")






