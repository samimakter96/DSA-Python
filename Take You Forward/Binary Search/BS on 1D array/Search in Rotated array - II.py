def search_rotate_array(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        # if mid points to the target
        if nums[mid] == target:
            return True

        # Handling Duplicates
        if nums[low] == nums[mid] and nums[mid] == nums[high]:
            low = low + 1
            high = high - 1
            continue  # Move to the next iteration

        # if the left part is sorted
        if nums[low] <= nums[mid]:
            if (nums[low] <= target) and (target <= nums[mid]):
                # the element exists
                high = mid - 1
            else:
                # the element does not exist
                low = mid + 1
        else:
            # if the right part is sorted
            if (nums[mid] <= target) and (target <= nums[high]):
                # if the element exists
                low = mid + 1
            else:
                # if the element does not exist
                high = mid - 1
    return False


nums = [2, 5, 6, 0, 0, 1, 2]
target = 0
print(search_rotate_array(nums, target))