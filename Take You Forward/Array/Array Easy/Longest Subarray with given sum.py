"""
Example 1:
Input Format: N = 3, k = 5, array[] = {2,3,5}
Result: 2
Explanation: The longest subarray with sum 5 is {2, 3}. And its length is 2.
"""
# Brute Force Approach 1:
arr = [2, 3, 5]
k = 5
n = len(arr)   # size of the array
length = 0
for i in range(n):  # starting index
    for j in range(i, n):   # ending index
        # add all the elements of
        # subarray = arr[i...j]:
        sum_subarray = 0
        for x in range(i, j+1):
            sum_subarray = sum_subarray + arr[x]
        if sum_subarray == k:
            length = max(length, j-i+1)
            # j - i + 1: This represents the length of the current subarray.
            # Suppose you find a subarray [2, 3] with a sum of 5
            # The length of this subarray is 2 (j - i + 1 where j = 1 and i = 0).
            # At this point, length is 0 because you haven't found any sub_arrays yet.
            # The line length = max(length, 2) compares 0 and 2 and sets length to 2
print(f"the length of the longest subarray is: {length}")

# Time Complexity: O(N^3)   Space Complexity: O(N)

# Brute Force Approach 2:
a = [2, 3, 5, 1, 9]
k = 10
n = len(a)
length = 0
for i in range(n):
    s = 0
    for j in range(i, n):
        s = s + a[j]
        if s == k:
            length = max(length, j-i+1)
print(f"the length of the longest subarray is: {length}")
# Time Complexity: O(N^2)  Space Complexity: O(1)


# Better Solution: USing Hashing / Dictionary

arr = [2, 3, 5, 1, 9]
k = 10
n = len(arr)

pre_sum = {}
curr_sum = 0
max_len = 0
for i in range(n):
    curr_sum += arr[i]
    # if curr_sum == k, updated the max_len
    if curr_sum == k:
        max_len = max(max_len, i+1)  # i + 1 represents the length of the subarray from index 0 to the current index.
    # calculate the sum of the remaining part
    rem = curr_sum - k
    if rem in pre_sum:
        length = i - pre_sum[rem]
        max_len = max(max_len, length)
    # of yes, update the dictionary with the current_sum and its index.
    if curr_sum not in pre_sum:
        pre_sum[curr_sum] = i
print(f"the length of the longest subarray is {max_len}")

# Time Complexity: O(N)   Space Complexity: O(N)


# Optimal Solution : Using two pointer
a = [2, 3, 5, 1, 9]
k = 10
n = len(a)
left, right = 0, 0   # two pointers
Sum = a[0]
max_len = 0
while right < n:
    # if sum > k, reduce the subarray from left
    # until sum becomes less or equal to k:
    while Sum > k and left <= right:
        Sum = Sum - a[left]
        left += 1

    # if sum = k, update the maxLen i.e. answer:
    if Sum == k:
        max_len = max(max_len, right-left + 1)
    # Move forward the right pointer: increment by 1
    right += 1
    # if right < n , increment Sum += a[right]
    if right < n:
        Sum = Sum + a[right]
print(max_len)

# Time Complexity : O(2*N) -> O(N)   Space Complexity : O(1)
