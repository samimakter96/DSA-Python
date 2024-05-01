"""
A trio is said to be perfect if first element is less than second and second element is less than third .
You have given an array of integer you have to find how many such perfect trios are there in the array .

Example:

Input:
arr = [1, 2, 3, 4]
Output: 4
Explanation: Fours perfect trios are (1, 2, 3), (1, 2, 4), (1, 3, 4) and (2, 3, 4).
"""


def count_trio(arr):

    n = len(arr)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if (arr[i] < arr[j]) and (arr[j] < arr[k]):
                    count = count + 1
    return count


nums = [1, 2, 3, 4]
print(count_trio(nums))