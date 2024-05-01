"""
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
"""

nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

i = m - 1  # Pointer for the last element in nums1
j = n - 1  # Pointer for the last element in nums2
k = m + n - 1  # Pointer for the last position in the merged array

while i >= 0 and j >= 0:
    if nums1[i] > nums2[j]:
        nums1[k] = nums1[i]
        i -= 1
    else:
        nums1[k] = nums2[j]
        j -= 1
    k -= 1

# If there are remaining elements in nums2, copy them to nums1
while j >= 0:
    nums1[k] = nums2[j]
    j -= 1
    k -= 1
print(nums1)