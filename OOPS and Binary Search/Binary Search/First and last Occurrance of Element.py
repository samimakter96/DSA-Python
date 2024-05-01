"""You are Given an array Sorted in ascending order. Find the Starting and ending Position of a given Target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,8,8,8,8,10], target = 8
Output: [3,8]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""


def first_last(arr, target):
    result = [-1, -1]  # Initialize result with -1 for cases where the target is not found

    # Search for the starting position
    st = 0
    end = len(arr) - 1
    while st <= end:
        mid = (st + end) // 2
        if target == arr[mid]:
            result[0] = mid
            end = mid - 1  # Adjust the search space to the left for finding the starting position
        elif target < arr[mid]:
            end = mid - 1
        else:
            st = mid + 1

    # Search for the ending position
    st = 0
    end = len(arr) - 1
    while st <= end:
        mid = (st + end) // 2
        if target == arr[mid]:
            result[1] = mid
            st = mid + 1  # Adjust the search space to the right for finding the ending position
        elif target < arr[mid]:
            end = mid - 1
        else:
            st = mid + 1

    return result


arr1 = [5, 7, 7, 8, 8, 10]
tar = 8
print(first_last(arr1, tar))
