"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.


Input: matrix=[[1,1,1],[1,0,1],[1,1,1]]

Output: [[1,0,1],[0,0,0],[1,0,1]]

Explanation: Since matrix[2][2]=0.There-fore the 2nd column and 2nd row wil be set to 0.
"""

# Brute Force Approach:


# def mark_row(matrix, n, m, i):
#     # set all non-zero elements as -1 in the row i:
#     for j in range(m):
#         if matrix[i][j] != 0:
#             matrix[i][j] = -1
#
#
# def mark_col(matrix, n, m, j):
#     # set all non-zero elements as -1 in the col j:
#     for i in range(n):
#         if matrix[i][j] != 0:
#             matrix[i][j] = -1
#
#
# def zero_matrix(matrix, n, m):
#     # Set -1 for rows and cols
#     # that contains 0. Don't mark any 0 as -1:
#     for i in range(n):
#         for j in range(m):
#             if matrix[i][j] == 0:
#                 mark_row(matrix, n, m, i)
#                 mark_col(matrix, n, m, j)
#
#     # Finally, mark all -1 as 0:
#     for i in range(n):
#         for j in range(m):
#             if matrix[i][j] == -1:
#                 matrix[i][j] = 0
#
#     return matrix
#
#
# matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
# n = len(matrix)
# m = len(matrix[0])
# print(zero_matrix(matrix, n, m))


# Better Approach:

matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
n = len(matrix)
m = len(matrix[0])

row = [0] * n   # row array
col = [0] * m   # col array

# Traverse the matrix
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0:
            # mark ith index row with 1:
            row[i] = 1
            # mark ith index col with 1:
            col[j] = 1

# Finally, mark all (i, j) as 0
# if row[i] or col[j] is marked with 1.
for i in range(n):
    for j in range(m):
        if row[i] or col[j]:
            matrix[i][j] = 0

print(matrix)

# Time Complexity: O(2*N*M)    Space Complexity: O(N)+O(M)


# Optimal Approach: