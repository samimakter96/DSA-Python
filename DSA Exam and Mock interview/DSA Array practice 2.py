"""
Q.1 write a program to sort the array based on how close it is to number 5
if the difference is the same then the element whose value is lesser will be before.
"""

arr = [1, 3, 5, 7, 9]
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if abs(arr[j] - 5) < abs(arr[i] - 5):
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
print(arr)


""" Q.2 A number is said to be sharpnerian number it the difference between any neighboring digits of number is 1
you have given a number x, you have to find all the x sharpnerian numbers
Note : Take difference as absolute difference and first sharpnerian number is 10 """

# phase 1: checking sharpnerian number True or False  if it is True then it's sharpnerian number


def is_sharpnerian(num):
    num_str = str(num)
    for i in range(len(num_str) - 1):
        if abs(int(num_str[i]) - int(num_str[i+1])) != 1:
            return False
    return True


def sharpnerian(n):
    sharpnerian_numbers = []
    current_number = 10  # The first sharpnerian number

    while len(sharpnerian_numbers) < n:
        if is_sharpnerian(current_number):
            sharpnerian_numbers.append(current_number)
        current_number += 1

    return sharpnerian_numbers


# Example: Find sharpnerian numbers up to 100


n = 2
result = sharpnerian(n)
print(result)


""" Q.3 Given an array of integers nums, write a function to count the number of bad pairs. A pair(i,j)is called bad
if nums[i] < nums[j] and i < j """

arr = [1, 2, 3, 1, 2, 3]
count = 0
for i in range(len(arr)-1):
    for j in range(i+1, len(arr)):
        if arr[j] > arr[i]:
            count = count+1
print(count)


""" Q.4 Given an array of integers and a target. you have to return the running sum if its equal to the target
      or greater than the target."""

a = [3, 4, 10, 15, 64]
target = 45
sum1 = 0
for i in range(len(a)):
    sum1 = sum1+a[i]
    if sum1 >= target:
        print(sum1)
        break
