from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # List to store the permutations
        result = []

        # Helper function for recursive permutation using swapping
        def recur_permute(index):
            # Base case: if the current index reaches the end, add the permutation to the result
            if index == len(nums):
                result.append(nums[:])
                return

            # Recursive permutation for each remaining element
            for i in range(index, len(nums)):
                # Swap the current element with the element at the current index
                nums[index], nums[i] = nums[i], nums[index]

                # Recursively call the function for the next index
                recur_permute(index + 1)

                # Backtrack by swapping back to the original positions
                nums[index], nums[i] = nums[i], nums[index]

        # Start the recursive permutation process
        recur_permute(0)

        return result


# Example usage:
if __name__ == "__main__":
    obj = Solution()
    input_nums = [1, 2, 3]
    permutations = obj.permute(input_nums)
    print("All Permutations are:")
    print(permutations)


# print all permutation of a given string

class Solution:
    def permute_string(self, s: str) -> List[str]:
        # Convert the string to a list for in-place swapping
        char_list = list(s)

        # List to store the permutations
        result = []

        # Helper function for recursive permutation using swapping
        def recur_permute(index):
            # Base case: if the current index reaches the end, add the permutation to the result
            if index == len(char_list):
                result.append("".join(char_list))
                return

            # Recursive permutation for each remaining character
            for i in range(index, len(char_list)):
                # Swap the current character with the character at the current index
                char_list[index], char_list[i] = char_list[i], char_list[index]

                # Recursively call the function for the next index
                recur_permute(index + 1)

                # Backtrack by swapping back to the original positions
                char_list[index], char_list[i] = char_list[i], char_list[index]

        # Start the recursive permutation process
        recur_permute(0)

        return result


# Example usage:
if __name__ == "__main__":
    obj = Solution()
    input_string = "abc"
    permutations = obj.permute_string(input_string)
    print("All Permutations are:")
    print(permutations)


# same approach using parameter
""" print All Permutation of a given array """


def permute_array(arr, start=0):
    # Base case: if the start index reaches the end of the array, print the permutation
    if start == len(arr):
        print(arr)
        return

    # Recursive permutation for each element at the start index
    for i in range(start, len(arr)):
        # Swap elements to generate permutations
        arr[start], arr[i] = arr[i], arr[start]

        # Recursively call the function for the next index
        permute_array(arr, start + 1)

        # Backtrack by swapping back to the original positions
        arr[start], arr[i] = arr[i], arr[start]


# Example usage:
input_array = [1, 2, 3]
print("All Permutations of {} are:".format(input_array))
permute_array(input_array)


""" Print All Permutation of a given string """


def permute_string(s, start=0):
    # Convert the string to a list to make it mutable
    char_list = list(s)

    # Base case: if the start index reaches the end of the string, print the permutation
    if start == len(s):
        print("".join(char_list))
        return

    # Recursive permutation for each character at the start index
    for i in range(start, len(s)):
        # Swap characters to generate permutations
        char_list[start], char_list[i] = char_list[i], char_list[start]

        # Recursively call the function for the next index
        permute_string("".join(char_list), start + 1)

        # Backtrack by swapping back to the original positions
        char_list[start], char_list[i] = char_list[i], char_list[start]


# Example usage:
input_string = "abc"
print("All Permutations of '{}' are:".format(input_string))
permute_string(input_string)
