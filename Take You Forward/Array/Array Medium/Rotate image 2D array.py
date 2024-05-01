"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate
another 2D matrix and do the rotation.

Example:1
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
"""

# Brute Force Approach:
# Approach: Take another dummy matrix of n*n, and then take the first row of the matrix and put it in the last column of
# the dummy matrix, take the second row of the matrix, and put it in the second last column of the matrix and so.

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n = len(matrix)
# Using a more traditional variable name (e.g., 'i') that isn't used inside the loop
rotated = []
for i in range(n):
    row = [0] * n  # Create a row filled with zeros
    rotated.append(row)  # Add the row to the 'rotated' matrix

for i in range(n):
    for j in range(n):
        rotated[j][n-i-1] = matrix[i][j]
print(rotated)

# Time Complexity: O(N^2)   Space Complexity: O(N^2)


# Optimal Approach:
# Approach:
# Step 1: Transpose the matrix. (transposing means changing columns to rows and rows to columns)
# Step 2: Reverse each row of the matrix.

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n = len(matrix)

# transposing the matrix
for row in range(n):
    for col in range(row, n):
        temp = matrix[row][col]
        matrix[row][col] = matrix[col][row]
        matrix[col][row] = temp

# reversing each row of the matrix
for row in matrix:
    row.reverse()
print(matrix)

# Time Complexity: O(N^2)   Space Complexity: O(1)
