"""
Given an m x n matrix, return all elements of the matrix in spiral order.

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
"""

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ans = []

rows = len(matrix)
cols = len(matrix[0])

top = 0
bottom = rows-1
left = 0
right = cols-1

# Loop un-till all element are not traversed
while top <= bottom and left <= right:

    # For moving left to right
    for i in range(left, right+1):
        ans.append(matrix[top][i])

    top += 1

    # For moving top to bottom
    for i in range(top, bottom+1):
        ans.append(matrix[i][right])

    right -= 1

    # For moving right to left
    if top <= bottom:
        for i in range(right, left-1, -1):
            ans.append(matrix[bottom][i])

        bottom -= 1

    # For moving bottom to top
    if left <= right:
        for i in range(bottom, top-1, -1):
            ans.append(matrix[i][left])

        left += 1
print(ans)