def search_rotated_array(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        # if mid points the target
        if nums[mid] == target:
            return mid

        # if the left part is sorted
        if nums[low] <= nums[mid]:
            if (nums[low] <= target) and (target <= nums[mid]):
                # element exits on the left part
                high = mid - 1
            else:
                # element does not exits on left
                low = mid + 1

        # if the right part is sorted
        else:
            if (nums[mid] <= target) and (target <= nums[high]):
                # element exits on the right part
                low = mid + 1
            else:
                # element does not exits on the right
                high = mid - 1
    return -1


nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
print(search_rotated_array(nums, target))