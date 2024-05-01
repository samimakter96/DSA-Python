"""
Given a square matrix . Return the maximum number from both diagonals.

Input:

1 2 3
4 5 6
7 8 9

Output: 9 7
Explanation: The maximum element in the diagonals is 9 and 7 respectively.
"""

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n = len(matrix)

max_left_diagonal = matrix[0][0]    # initialize max left diagonal then compare with others
for i in range(1, n):
    max_left_diagonal = max(max_left_diagonal, matrix[i][i])
print(max_left_diagonal)

max_right_diagonal = matrix[0][n-1]   # initialize max right diagonal then compare with others
for i in range(1, n):
    max_right_diagonal = max(max_right_diagonal, matrix[i][n-1-i])  # for -i if we want to move to the right
print(max_right_diagonal)


# Same Code for understanding
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

max_left_diagonal = arr[0][0]
for i in range(len(arr)):
    if arr[i][i] > max_left_diagonal:
        max_left_diagonal = arr[i][i]
print("Max Left Diagonal:", max_left_diagonal)

max_right_diagonal = arr[0][len(arr) - 1]
for i in range(len(arr)):
    if arr[i][len(arr) - 1 - i] > max_right_diagonal:
        max_right_diagonal = arr[i][len(arr) - 1 - i]
print("Max Right Diagonal:", max_right_diagonal)
