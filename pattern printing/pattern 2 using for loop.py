# 1. left side triangle
# n = int(input("Enter the number of row:"))
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print("*", end="")
#     print()

# 2. print 1
# num = int(input("Enter the number of row:"))
# k = 1
# for i in range(1, num+1):
#     for j in range(1, k+1):
#         print("1", end="")
#     k = k+2
#     print()

# left side triangle downside
# n = int(input("Enter number of row:"))
# for i in range(n):
#     for j in range(n-i):
#         print("*", end="")
#     print()

# left side triangle upside
# n = int(input("Enter number of row"))
# for i in range(n):
#     for j in range(i+1):
#         print("*", end="")
#     print()

# right side triangle upside
# n = int(input("Enter number of row:"))
# for i in range(n):
#     for j in range(1, n-i):  # we start from 1 because we need only 4th space row
#         print("-", end="")
#     # print()
#     for j in range(i+1):
#         print("*", end="")
#     print()

# right side triangle downside
# n = 5
# for i in range(n):
#     for j in range(1, i+1):  # we start from 1 because space start from second row (only 4th space row)
#         print(" ", end="")
#     # print()
#     for j in range(n-i):
#         print("*", end="")
#     print()

# Hill pattern
# n = int(input("Enter row number:"))
# for i in range(n):
#     for j in range(1, n-i):
#         print(" ", end="")
#     # print()
#     for j in range(1, i+1):  # we start from 1 because we need only 1 * in the top
#         print("*", end="")
#     # print()
#     for j in range(i+1):
#         print("*", end="")
#     print()

""" Binary triangle pattern """


def pattern1(N):
    # First row starts by printing a single 1.
    start = 1

    # Outer loop for the number of rows
    for i in range(N):

        # If the row index is even, then 1 is printed first in that row.
        if i % 2 == 0:
            start = 1

        # If odd, then the first 0 will be printed in that row.
        else:
            start = 0

        # We alternatively print 1's and 0's in each row by using the inner for loop.
        for j in range(i + 1):
            print(start, end="")
            start = 1 - start

        # As soon as the numbers for each iteration are printed, we move to the
        # next row and give a line break; otherwise, all numbers
        # would get printed in 1 line.
        print()


# Example usage:
N = 5
pattern1(N)

# number crown pattern
# n = 5
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     for j in range(n-i):
#         print(" ", end=" ")
#     for j in range(n-i):
#         print(" ", end=" ")
#     for j in range(i, 0, -1):
#         print(j, end=" ")
#     print()

# increasing number triangle pattern
# n = 5
# num = 1
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(num, end=" ")
#         num = num + 1
#     print()

# increasing letter triangle pattern


def pattern2(N):
    # Outer loop for the number of rows.
    for i in range(N):
        # Inner loop will loop for i times and
        # print alphabets from 'A' to 'A' + i.
        for ch in range(ord('A'), ord('A') + i + 1):
            print(chr(ch), end=" ")

        print()


N = 5
pattern2(N)

# Decreasing letter triangle
n = 5
for i in range(n):
    for ch in range(ord('A'), ord('A') + n - i):
        print(chr(ch), end=" ")
    print()


# Alpha Ramp pattern
def pattern16(N):
    # Outer loop for the number of rows.
    for i in range(N):
        for j in range(i + 1):
            # The same character, which is defined,
            # is to be printed i times in that row.
            print(chr(ord('A') + i), end=" ")
        print()


N = 5
pattern16(N)

# Alpha Hill pattern
n = 4
for i in range(n):
    for j in range(1, n-i):
        print(" ", end=" ")
    # print()
    for ch in range(ord('A'), ord('A') + i + 1):
        print(chr(ch), end=" ")
    # print()
    for j in range(i, 0, -1):
        print(chr(ord('A') + j - 1), end=" ")
    print()

# Alpha triangle pattern
# n = 5
# for i in range(n):
#     for ch in range(ord('A')+n-1-i, ord('A')+n):
#         print(chr(ch), end=" ")
#     print()


# n = 5
# for row in range(n):
#     for col in range(row+1):
#         print(chr((n - col) + 64), end=" ")
#     print()

# Rectangle pattern
n = 5
for row in range(n):
    for col in range(n):
        if (col == 0 or col == n-1) or (row == 0 or row == n-1) and (col > 0 and col < n-1):
            print("*", end=" ")
        else:
            print(end="  ")
    print()
