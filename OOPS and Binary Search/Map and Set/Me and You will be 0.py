"""
You are given a array with positive and negative numbers .
you have to find the part of the array i.e subarray which has addition 0 .
the output should be true if subarray present in array whose sum is 0 and return false if not.

Solve it in 0(n).

Example 1:
Input: 5 4 2 -3 1 6
Output: True
Explanation: 2, -3, 1 is the subarray with sum 0.
"""


def has_subarray_with_sum_zero(nums):
    prefix_sum = {0: -1}    # store prefix sums with the initial value of 0 at index -1.
    current_sum = 0

    # Iterating through the array
    for i, num in enumerate(nums):
        current_sum += num

        # Checking if the current prefix sum is already in the dictionary
        if current_sum in prefix_sum:
            # Found a subarray with sum 0
            return True
        else:
            # Store the current prefix sum along with its index
            prefix_sum[current_sum] = i

    # No subarray with sum 0 found
    return False


# Example Usage:
arr = [5, 4, 2, -3, 1, 6]
print(has_subarray_with_sum_zero(arr))  # Output: True

# Same problem but without using enumerate function


def has_subarray_with_sum_zero(nums):
    prefix_sum = {0: -1}    # store prefix sums with the initial value of 0 at index -1.
    current_sum = 0
    index = -1  # Initialize index manually we use -1 because indexing stars from 0 so, after 1 iteration in become 0

    # Iterating through the array
    for num in nums:
        index += 1  # Manually increment the index

        # Updating the current prefix sum
        current_sum += num

        # Checking if the current prefix sum is already in the dictionary
        if current_sum in prefix_sum:
            # Found a subarray with sum 0
            return True
        else:
            # Store the current prefix sum along with its index
            prefix_sum[current_sum] = index

    # No subarray with sum 0 found
    return False


# Example Usage:
arr = [5, 4, 2, -3, 1, 6]
print(has_subarray_with_sum_zero(arr))  # Output: True


"""
Prefix Sum:
Prefix sum is an array where each element represents the sum of all elements before it in the original array.
It helps us quickly compute the sum of any subarray.

Two-Prefix Sum:
While iterating through the array, keep track of the running sum.
If the same running sum occurs again, it means there's a subarray with a specific sum

Let's take an array [5, 4, 2, -3, 1, 6] and compute the two-prefix sum:

Original Array: [5, 4, 2, -3, 1, 6]
Prefix Sum Array: [0, 5, 9, 11, 8, 9, 15]

If you observe, the value 9 occurs twice in the prefix sum array (at indices 2 and 5). This indicates that the subarray
between these indices [2, -3, 1] has a sum of 0.
"""
