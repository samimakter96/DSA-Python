arr = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
maximum = 0     # this will only work in positive number
n = len(arr)
for i in range(0, n):
    sum_ = 0
    for j in arr[i]:
        sum_ = sum_+j
    if sum_ > maximum:
        maximum = sum_
print("Maximum =", maximum)


arr = [[-1, -5], [-7, -3], [-3, -5]]
max_val = sum(arr[0])
for row in range(len(arr)):
    sum_val = 0
    for colum in arr[row]:
        sum_val = sum_val + colum
    if sum_val > max_val:
        max_val = sum_val
print("Maximum value is =", max_val)


arr = [[1, 5], [7, 3], [3, 5]]
maxi = sum(arr[0])
for row in arr:
    sum_ = 0
    for element in row:
        sum_ += element
        if sum_ > maxi:
            maxi = sum_
print(maxi)

# solution 2:
arr = [[-1, -5], [-7, -3], [-3, -5]]
max_val = sum(arr[0])  # Initialize max_val with the sum of the first row
for row in range(1, len(arr)):  # Start the loop from the second row (index 1)
    sum_val = sum(arr[row])  # Calculate the sum of the current row
    if sum_val > max_val:
        max_val = sum_val
print("Maximum value is =", max_val)
