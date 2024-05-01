def print_subsequences(arr, index, subarr):
    # Base case: If we have reached the end of the array
    if index == len(arr):
        # Check if the current subsequence is not empty, then print it
        if len(subarr) != 0:
            print(subarr)
    else:
        # Recursive call without including the current element in the subsequence
        print_subsequences(arr, index + 1, subarr)

        # Recursive call including the current element in the subsequence
        print_subsequences(arr, index + 1, subarr + [arr[index]])

        subarr.pop()


# Example usage
arr = [1, 2, 3]
print_subsequences(arr, 0, [])


from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    # Function to generate all subsets of a given list of numbers
    def generate_subsets(index, current_subset):
        # Base case: If we have considered all elements
        if index == len(nums):
            # Include the current subset in the result
            result.append(current_subset[:])    # current_subset[:] ensures that each subset in the result is
                                                # independent of the others.
            return

        # Recursive call without including the current element in the subset
        generate_subsets(index + 1, current_subset)

        # Recursive call including the current element in the subset
        current_subset.append(nums[index])
        generate_subsets(index + 1, current_subset)

        # Backtrack to maintain the original state of the subset
        current_subset.pop()

    # List to store the final result
    result = []

    # Start generating subsets from the first index with an empty subset
    generate_subsets(0, [])

    return result


# Example usage
nums = [1, 2, 3]
result = subsets(nums)
print(result)

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def generate_subsets(index, subarr):
            result.append(subarr[:])  # Append a copy of the current subarray to the result

            for i in range(index, len(nums)):
                subarr.append(nums[i])  # Include the current element in the subarray
                generate_subsets(i + 1, subarr)  # Recursively generate subsets
                subarr.pop()  # Backtrack by removing the last element

        generate_subsets(0, [])
        return result


# Example usage
nums = [1, 2, 3]
solution = Solution()
output = solution.subsets(nums)
print(output)


def generate_subset(index, curr_subset):

    if index == len(nums):
        print(curr_subset)
        return

    generate_subset(index + 1, curr_subset)

    generate_subset(index + 1, curr_subset + nums[index])


nums = "abc"
generate_subset(0, "")
