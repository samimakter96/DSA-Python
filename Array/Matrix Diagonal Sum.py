"""
Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.
"""

mat = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

n = len(mat)
sum_diagonal = 0
for i in range(n):
    sum_diagonal += mat[i][i]     # primary diagonal
    sum_diagonal += mat[i][len(mat)-1 - i]   # secondary diagonal

middle = mat[n//2][n//2]

if len(mat) % 2 != 0:   # if the matrix length odd then we count the middle only once that's why we remove the middle
    print(sum_diagonal - middle)
else:
    print(sum_diagonal)  # if it's even we don't have to do anything just return sum_diagonal
