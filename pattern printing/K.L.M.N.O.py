# 11. K pattern:
# i = 0
# j = 4
# for row in range(7):
#     for col in range(5):
#         if col == 0 or (row == col+2 and col > 1):
#             print("*", end="  ")
#         elif row == i and col == j:
#             print("*", end="  ")
#             i = i+1
#             j = j-1
#         else:
#             print(end="  ")
#     print()

# 12. L Pattern:
# for row in range(7):
#     for col in range(5):
#         if col == 0 or (row == 6 and col > 0):
#             print("*", end=" ")
#         else:
#             print(end=" ")
#     print()

# 13. M pattern:
# for row in range(7):
#     for col in range(7):
#         if (col == 0 or col == 6 or ((row == col) and (col > 0 and col < 4)) or
#         row == 1 and col == 5 or (row == 2 and col == 4)):
#             print("*", end=" ")
#         else:
#             print(end="  ")
#     print()

# 14. N Pattern:
# for row in range(7):
#     for col in range(7):
#         if (col == 0 or col == 6) or ((row == col) and (col > 0 and col < 6)):
#             print("*", end=" ")
#         else:
#             print(end="  ")
#     print()

# 15. O pattern:
for row in range(7):
    for col in range(5):
        if ((col == 0 or col == 4) and (row != 0 and row != 6)) or ((row == 0 or row == 6) and (col != 0 and col != 4)):
            print("*", end=" ")
        else:
            print(end="  ")
    print()