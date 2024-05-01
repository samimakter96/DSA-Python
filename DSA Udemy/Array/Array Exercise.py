# Array/List Exercise:
# project-1
"""Find numbers of days above average temperature"""
num_days = int(input("How many day's temperature?:"))
total = 0
temp = []
for i in range(num_days):
    next_days = int(input("Day " + str(i+1) + "'s high temperature:"))
    temp.append(next_days)
    total += temp[i]

avg = round(total/num_days, 2)
print("Average =" + str(avg))

above = 0
for i in temp:
    if i > avg:
        above += 1

print(str(above) + " day's above average")


"""Q.1 Missing number"""


def missing_number(arr, n):
    # Calculate the sum of first n natural numbers
    total = n * (n + 1) // 2

    # Calculate the sum of numbers in the array
    sum_arr = sum(arr)

    # Find the missing number by subtracting sum_arr from total
    missing = total - sum_arr

    return missing

# Time Complexity: O(n) because it iterates through the array once to calculate the sum of its elements.


# Example
print(missing_number([1, 2, 3, 4, 6], 6))  # Output: 5


"""Q.2 pairs/two sum"""


# def find_pairs(nums, target):
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i, j]
#
#
# my_list = [2, 7, 11, 15]
# print(find_pairs(my_list, 9))

# Time Complexity: O(n^2)  Space Complexity: O(1)

# Optimal Approach:

def two_sum(arr, target):
    seen_dic = {}
    for i, num in enumerate(arr):
        complement = target - num

        if complement in seen_dic:
            return [seen_dic[complement], i]
        seen_dic[num] = i


nums = [2, 7, 11, 15]
tar = 9
print(two_sum(nums, tar))
# Time Complexity: O(n)  Space Complexity: O(1)

"""Q.3 Max product of two integers"""


# def max_product(arr):
#     max1 = 0
#     max2 = 0
#     for i in arr:
#         if i > max1:
#             max2 = max1
#             max1 = i
#         elif i > max2 and i != max1:
#             max2 = i
#     return max1 * max2
#
#
# a = [1, 7, 3, 4, 9, 5]
# print(max_product(a))

# Time Complexity: O(n)   Space Complexity: O(1)

"""Given 2D list calculate the sum of diagonal elements."""


def diagonal_sum(matrix):
    total = 0
    for i in range(len(matrix)):
        total = total + matrix[i][i]

    return total


myList2D = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(diagonal_sum(myList2D))   # output: 1+5+9 = 15
# Time Complexity: O(n)   Space Complexity: O(1)

"""Q.4 Given a list, write a function to get first, second best scores from the list."""


def first_second(my_list):
    first = float('-inf')   # Set their initial values to negative infinity.
    second = float('-inf')

    for num in my_list:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return first, second


arr = [84, 85, 86, 87, 85, 90, 85, 83, 23, 45, 84, 1, 2, 0]
print(first_second(arr))
# Time Complexity: O(n)   Space Complexity: O(1)

"""Q.5 Write a function to remove the duplicate numbers on given integer array/list."""


def remove_duplicates(arr):
    unique_lst = []
    seen = set()

    for item in arr:
        if item not in seen:    # when i not in seen then it add
            unique_lst.append(item)
            seen.add(item)
    return unique_lst


my_list = [1, 1, 2, 2, 3, 4, 5]
print(remove_duplicates(my_list))
# Time Complexity: O(n)   Space Complexity: O(n)

"""Q.6 Write a function to find all pairs of an integer array whose sum is equal to a given number. Do not consider 
commutative pairs."""


def pair_sum(arr, target):
    result = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                result.append(f"{arr[i]}+{arr[j]}")
    return result


my_list = [2, 4, 3, 5, 6, -2, 4, 7, 8, 9]
target_sum = 7
print(pair_sum(my_list, target_sum))
# Time Complexity: O(n^2)   Space Complexity: O(n)

"""Q.7 Given an integer array nums, return true if any value appears at least twice in the array, and return false 
if every element is distinct."""


def contains_duplicate(nums):
    # Step 1: Create an empty set to store unique elements
    unique_elements = set()

    # Step 2: Loop through each element in the array
    for num in nums:
        # Step 3: Check if the element is already in the set
        if num in unique_elements:
            # If yes, a duplicate is found, return True
            return True
        else:
            # If not, add the element to the set
            unique_elements.add(num)

    # Step 4: If the loop completes without finding duplicates, return False
    return False


# Example usage:
nums = [1, 2, 3, 1, 4, 5]
result = contains_duplicate(nums)
print(result)

# Time Complexity: O(n)   Space Complexity: O(n)


"""Q.8 Permutation"""


# def permutation(list1, list2):
#     if len(list1) != len(list2):
#         return False
#     list1.sort()
#     list2.sort()
#     if list1 == list2:
#         return True
#     else:
#         return False
#
#
# arr1 = [1, 2, 3]
# arr2 = [2, 1, 3]
# print(permutation(arr1, arr2))
# num1 = ['a', 'b', 'c']
# num2 = ['c', 'a', 'b']
# print(permutation(num1, num2))
# word1 = ['r', 'a', 'i', 'l']
# word2 = ['l', 'a', 'i', 'r']
# print(permutation(word1, word2))


"""Q.9 Rotate Matrix"""


def rotate(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            # Swap the elements at positions (i, j) and (j, i)
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            # matrix[i][j], matrix[j][i]
            # matrix[0][1] is swapped with matrix[1][0].

    # Reverse each row
    for row in matrix:
        row.reverse()
    return matrix


matrix2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(rotate(matrix2d))

# Time Complexity: O(n^2)   Space Complexity: O(1)
