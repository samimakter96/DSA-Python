# 16. P pattern:
# for row in range(7):
#     for col in range(5):
#         if col == 0 or (col == 4 and (row == 1 or row == 2)) or ((row == 0 or row == 3) and (col > 0 and col < 4)):
#             print("*", end=" ")
#         else:
#             print(end="  ")
#     print()

# 17. Q pattern:
# for row in range(8):
#     for col in range(5):
#         if (((col == 0 or col == 4) and (row > 0 and row < 6)) or ((row == 0 or row == 6) and (col > 0 and col < 4))
#                 or ((row == 5 and col == 1) or (row == 7 and col == 3))):
#             print("*", end=" ")
#         else:
#             print(end="  ")
#     print()

# 18. R pattern:
# for row in range(7):
#     for col in range(5):
#         if col == 0 or ((col == 4 and (row != 0 and row != 3)) or ((row == 0 or row == 3)) and (col > 0 and col < 4)):
#             print("*", end=" ")
#         else:
#             print(end="  ")
#     print()

# 19. S pattern
# for row in range(7):
#     for col in range(5):
#         if ((row == 0 or row == 3 or row == 6) and (col > 0 and col < 4) or (col == 0 and (row > 0 and row < 3)) or
#                 (col == 4 and (row > 3 and row < 6))):
#             print("*", end=" ")
#         else:
#             print(end="  ")
#     print()

# 20. T pattern
for row in range(7):
    for col in range(5):
        if col == 2 or (row == 0 and col != 2):
            print("*", end=" ")
        else:
            print(end="  ")
    print()