"""
A peak element is an element that is strictly greater than its neighbors.
Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks,
return the index to any of the peaks.

Example 1:
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
"""


def find_peak(arr):

    n = len(arr)    # edge case this is because an array of length 1 is considered a peak
    if n == 1:
        return 0

    left = 0
    right = len(arr)-1
    while left <= right:
        mid = (left + right) // 2
        
        # check if mid is a peak
        if (mid == 0 or arr[mid] > arr[mid-1]) and (mid == len(arr)-1 or arr[mid] > arr[mid+1]):
            return mid
        # If the left mid neighbour is greater than the mid, search in the left half
        elif mid > 0 and arr[mid - 1] > arr[mid]:
            right = mid - 1
        else:
            # If the right mid neighbor is greater than the mid, search in the right half
            left = mid + 1

    return -1   # Return -1 if no peak is found


nums = [1, 2, 3, 1]
print(find_peak(nums))