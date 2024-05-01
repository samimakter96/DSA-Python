"""Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums,
or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
"""

# Approach 1:


def target_index(arr):

    left = 0
    right = len(arr)-1
    # calculate mid
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid

        # left side portion
        elif arr[mid] >= arr[left]:
            # if it's true it means the target element is in the left side
            if (target >= arr[left]) and (target <= arr[mid]):
                right = mid - 1
            else:
                left = mid + 1

        # right side
        # if arr[mid] <= arr[right]:
        else:
            # it means the target element is in the right side.
            if (target >= arr[mid]) and (target <= arr[right]):
                left = mid + 1
            else:
                right = mid - 1
    return -1


arr = [4, 5, 6, 7, 0, 1, 2]
target = 0

print(target_index(arr))


# Approach 2:
def find_index(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            return mid

        # left sorted portion
        if nums[left] <= nums[mid]:
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[left]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            elif target > nums[left]:
                right = mid - 1

            # if nums[left] <= nums[mid]:
            #     if target > nums[mid] or target < nums[left]:
            #         left = mid + 1
            #     else:
            #         right = mid - 1

        # right sorted portion
        else:
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[right]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                right = mid - 1

            # if target > nums[mid] or target < nums[right]:
            #     left = mid + 1
            # else:
            #     right = mid - 1
    return - 1


arr = [4, 5, 6, 7, 0, 1, 2],
target1 = [0]
print(find_index(arr, target1))
