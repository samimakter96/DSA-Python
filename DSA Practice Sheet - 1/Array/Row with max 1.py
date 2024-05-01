"""
Given a boolean 2D array of n x m dimensions where each row is sorted. Find the 0-based index of the first row that
has the maximum number of 1's.
"""

arr = [[0, 0, 3, 1], [1, 2, 1, 3, 1, 1], [5, 6, 1, 2, 1]]

max_count = 0
max_count_row_index = -1  # Initialize with an invalid index

for i, row in enumerate(arr):
    count = row.count(1)
    if count > max_count:
        max_count = count
        max_count_row_index = i

if max_count_row_index != -1:
    print("Row with the maximum count of 1s:", max_count_row_index)
else:
    print("No row contains the element 1.")

# Same Approach but without using enumerate and count function
arr = [[0, 0, 3, 1], [1, 2, 1, 3, 1, 1], [5, 6, 1, 2, 1]]

max_count = 0
max_count_row_index = -1
row_index = 0
for row in arr:
    count = 0
    for col in row:
        if col == 1:
            count += 1
    if count > max_count:
        max_count = count
        max_count_row_index = row_index
    row_index += 1

print(max_count_row_index)

# Time Complexity: O(n * m)  n = row, m = col
# Space Complexity: O(1)

