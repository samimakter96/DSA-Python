
def next_permutation(nums):

    # step-1: find the break point
    ind = -1    # break point
    for i in range(len(nums)-2, -1, -1):    # we start traversing from reverse order
        if nums[i] < nums[i+1]:
            ind = i     # index i is the break point
            break

    # if break point dosent exits
    if ind == -1:
        nums.reverse()
        return nums

    # step-2: find the next greater element who is just greater than nums[ind] and swap it with
    for i in range(len(nums)-1, ind, -1):
        if nums[i] > nums[ind]:
            nums[i], nums[ind] = nums[ind], nums[i]
            break

    # step-3: reverse the right half nums[ind+1] to last of the array
    nums[ind+1:] = reversed(nums[ind+1:])

    return nums


nums = [1, 3, 2]
print(next_permutation(nums))


# Time Complexity: O(3N)    Space Complexity: O(1)
