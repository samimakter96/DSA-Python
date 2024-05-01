# Find the maximum of an array

arr = [5, 4, 7, 2, 6]
maximum = arr[0]
for i in range(len(arr)):
    if arr[i] > maximum:
        maximum = arr[i]
print("Maximum number =", maximum)

# # Example 2:
arr = [-5, -3, -4, -2, -7, -6, -8, -9, -1, -4]
maximum = arr[0]
for i in range(len(arr)):
    if arr[i] > maximum:
        maximum = arr[i]
print(maximum)

#  Find the minimum of an array

a = [5, 6, 2, 9, -2]
minimum = a[0]
for i in range(len(a)):
    if a[i] < minimum:
        minimum = a[i]
print(minimum)

# # Example 2
a = [12, 23, 45, 34, 67, 89, 31]
minimum = a[0]
for i in range(len(a)):
    if a[i] < minimum:
        minimum = a[i]
print(minimum)
