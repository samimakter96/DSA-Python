# left Upper side
# n = int(input("Enter the number of row:"))
# i = 1
# while i <= n:
#     j = 1
#     while j <= i:
#         print("*", end=" ")
#         j = j + 1
#     print()
#     i = i + 1

# Example 2: same as just print i
# n = int(input("Enter the number of row:"))
# i = 1
# while i <= n:
#     j = 1
#     while j <= i:
#         print(i, end=" ")
#         j = j + 1
#     print()
#     i = i + 1

# Example 3: same as just print j
# n = int(input("Enter the number of row:"))
# i = 1
# while i <= n:
#     j = 1
#     while j <= i:
#         print(j, end=" ")
#         j = j + 1
#     print()
#     i = i + 1

# n = 5
# for i in range(1,n+1):
#     for j in range(n+1,i,-1):
#         print("*", end="")
#     print()
#     for k in range(i):
#         print("*", end="")
#     print()


# left downside pattern
# i = 5
# while i > 0:
#     j = i
#     while j > 0:
#         print("*", end="")
#         j = j - 1
#     print()
#     i = i - 1

# left upside pattern
n = 5
i = 1
while i <= n:
    j = 1
    while j <= i:
        print("*", end="")
        j = j + 1
    print()
    i = i + 1


