"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that
is missing from the array.

Example 1:
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the
range since it does not appear in nums.
"""

# Brute Force Approach:

arr = [1, 2, 3, 5]
n = len(arr)

for i in range(1, n+1):
    flag = 0    # we initialize flag = 0 means the element is missing
    for j in range(n):
        if arr[j] == i:
            flag = 1    # flag = 1 means the element is present
            break
    if flag == 0:   # after iterating if flag still become = 0 that mean we found our missing number
        print(i)
# TC --> O(N^2)   SC --> O(1)


# Optima Solution:


def missing_number(a, N):
    # summation of first N numbers
    summation = (N * (N+1)) // 2
    actual_sum = sum(a)
    missing_num = summation - actual_sum
    return missing_num


arr = [1, 3, 2, 5]
N = 5
print(missing_number(arr, N))

# TC --> O(N)   SC --> O(1)


# Optimal Solution: 2
arr = [1, 2, 4, 5]
n = len(arr)
xor1 = 0
for i in range(1, n+1):    # XOR up to [1...N]
    xor1 = xor1 ^ i

xor2 = 0
for i in range(n-1):
    xor2 = xor2 ^ arr[i]    # XOR of array elements

print(xor1 ^ xor2)


def missingNumber(a, N):
    xor1 = 0
    xor2 = 0

    for i in range(N - 1):
        xor2 = xor2 ^ a[i]  # XOR of array elements
        xor1 = xor1 ^ (i + 1)  # XOR up to [1...N-1]

    xor1 = xor1 ^ N  # XOR up to [1...N]

    return xor1 ^ xor2  # the missing number


N = 5
arr = [1, 2, 3, 5]
print(missingNumber(arr, N))
