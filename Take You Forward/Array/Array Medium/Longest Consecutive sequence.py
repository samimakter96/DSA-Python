"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""


# Better Solution:


def longest_consecutive_element(a):

    n = len(a)
    if n == 0:
        return 0

    # sort the array
    a.sort()
    last_smaller = float('inf')
    count = 0
    longest = 1

    for i in range(n):
        if a[i] - 1 == last_smaller:
            count += 1
            last_smaller = a[i]

        elif a[i] != last_smaller:
            count = 1
            last_smaller = a[i]

        longest = max(longest, count)

    return longest


nums = [100, 4, 200, 1, 3, 2]
print(longest_consecutive_element(nums))

# Time Complexity: O(N log N)   Space Complexity: O(1)


# Optimal Solution: Using Set

nums = [100, 4, 200, 1, 3, 2]
n = len(nums)

longest = 1
st = set()
# put all array element into set
for i in range(n):
    st.add(nums[i])

# find the longest sequence
for element in st:
    # element is a starting number
    if element - 1 not in st:
        count = 1
        x = element
        while x + 1 in st:
            x = x + 1
            count += 1

        longest = max(longest, count)
print(longest)
