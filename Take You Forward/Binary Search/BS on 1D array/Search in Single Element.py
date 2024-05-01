def search_single_element(nums):
    n = len(nums)

    # Edge Cases:
    if n == 1:
        return nums[0]
    # first element
    if nums[0] != nums[1]:
        return nums[0]
    # last element
    if nums[n - 1] != nums[n - 2]:
        return nums[n - 1]

    low = 1
    high = n - 2
    while low <= high:
        mid = (low + high) // 2

        if nums[mid] != nums[mid + 1] and nums[mid] != nums[mid - 1]:
            return nums[mid]
        # if we are in left side
        if (mid % 2 == 0 and nums[mid] == nums[mid + 1]) or (mid % 2 == 1 and nums[mid] == nums[mid - 1]):
            low = mid + 1
        # we are in right side
        else:
            high = mid - 1
    return - 1


nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]

print(search_single_element(nums))
