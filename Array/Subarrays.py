# print subarray using while loop
arr = [1, 2, 3, 4, 5]
n = len(arr)
i = 0
while i < n:
    j = i
    while j < n:
        k = i
        while k <= j:
            print(arr[k], end=" ")
            k = k+1
        print()  # this print() for new line
        j = j+1
    i = i+1

# print subarray using for loop
arr = [1, 2, 3, 4, 5, 6]
n = len(arr)
for i in range(n):
    for j in range(i, n):
        for k in range(i, j+1, 1):
            print(arr[k], end=" ")
        print("\n", end="")   # this is for new_line also


# Example 2
# a = [1, 2, 3, 4, 5]
# for i in range(0,len(a)):
#     for j in range(i, len(a)):
#         str1 = ""
#         for k in range(i, j +1):
#             str1 = str1+str(a[k])
#         print(str1)

arr = [1, 2, 3, 4, 5, 6, 7]
n = len(arr)
for i in range(n):
    for j in range(i, n):
        for k in range(i, j+1, 1):
            print(arr[k], end=" ")
        print()  # this is for new line
