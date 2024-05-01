# Q.1 write a program to find the missing number that when add to it become divisible by 69
"""
input: 123
output: 15
Explanation: if we subtract 123+15 = 138 which is divisible by 69.
"""
num = 123
count = 0
temp = num

while num % 69 != 0:
    count = count + 1
    num = num + count
    if num % 69 == 0:
        print(num - temp)


""" Q.2 Given an (m x n) 2d array count the number of 5 in it."""

arr = [[1, 2, 5], [3, 5, 5]]

count = 0
for row in arr:
    for element in row:
        if element == 5:
            count += 1
print("Total 5 is =", count)

# solution 2:
arr = [[1, 2, 5], [3, 5, 5]]
count = 0
for i in range(len(arr)):
    for j in arr[i]:
        if j == 5:
            count += 1
print("Total 5 is =", count)


""" Q.3 A students total marks is the amount of marks they have in all their exams.
     The topper student is the student that has the maximum marks. """

arr = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
max_marks = 0
for i in range(len(arr)):
    sum_ = 0
    for j in arr[i]:
        sum_ += j
        if sum_ > max_marks:
            max_marks = sum_
print(max_marks)

# solution 2:
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
maxi = sum(arr[0])
for i in range(1, len(arr)):
    sum_ = sum(arr[i])
    if sum_ > maxi:
        maxi = sum_
print(maxi)

"""
Q.4 you have given array of marks of students. A topper is a student whose marks are greater than marks of all the
students present at its right.
The student at last of array will always a topper. you have to return marks of all the toppers in array
"""

arr = [16, 17, 4, 3, 5, 2]
topper = []
max_marks = -1
for i in range(len(arr)-1, -1, -1):
    if arr[i] > max_marks:
        max_marks = arr[i]
        topper.append(max_marks)
print(topper[::-1])


"""Q.5 An array of integers is given to returning the indices of those two elements whose product is equal to the target
input: nums = [1, 3, 5, 7, 8, 10] 
output: 2 5 """

nums = [1, 3, 5, 7, 8, 10]
n = len(nums)
target = 50
for i in range(n):
    for j in range(i + 1, n):
        if nums[i] * nums[j] == target:
            print(i, j)

# Optimal Solution: TC - O(N)  SC - O(N)
nums = [1, 3, 5, 7, 8, 10]
target = 50

num_map = {}
for i in range(len(nums)):
    complement = target / nums[i]
    if complement in num_map:
        print(num_map[complement], i)
    num_map[nums[i]] = i

# Approach 2: if there is any duplicate
nums = [1, 3, 5, 7, 8, 10]
n = len(nums)
target = 50

# Create a list to store the pairs of indices
pairs = []

for i in range(n):
    for j in range(i + 1, n):
        pr = nums[i] * nums[j]
        if pr == target:
            # Check if the pair is already in the list
            if (i, j) not in pairs and (j, i) not in pairs:
                pairs.append((i, j))

# Print the unique pairs of indices
for pair in pairs:
    print(pair)

"""Add two arr element"""
l1 = [1, 2, 3]
l2 = [2, 3, 4]

ans = []
for i in range(len(l1)):
    ans.append(l1[i] + l2[i])
print(ans)


"""Write a program to add two matrices (2d Array). return the result array"""
# Given matrices
mt1 = [[1, 2, 5], [3, 5, 5]]
mt2 = [[1, 5, 7], [2, 1, 3]]

# Initialize an empty matrix for the result
result_matrix = []

# Iterate through rows
for i in range(len(mt1)):
    # Initialize an empty row for the result_matrix
    result_row = []

    # Iterate through columns
    for j in range(len(mt1[0])):
        # Add the corresponding elements and append to the result_row
        result_row.append(mt1[i][j] + mt2[i][j])

    # Append the result_row to the result_matrix
    result_matrix.append(result_row)

# Print the result_matrix
for row in result_matrix:
    print(row)
