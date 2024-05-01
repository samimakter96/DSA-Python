# 21. U pattern:
# for row in range(7):
#     for col in range(5):
#         if ((col == 0 or col == 4) and (row < 6)) or ((row == 6) and (col > 0 and col < 4)):
#             print("*", end=" ")
#         else:
#             print(end="  ")
#     print()

# 22. V pattern:
# i = 0
# j = 6
# for row in range(4):
#     for col in range(7):
#         if row == col:
#             print("*", end=" ")
#         elif row == i and col == j:
#             print("*", end=" ")
#             i = i + 1
#             j = j - 1
#         else:
#             print(end=" ")
#     print()

# 23. W Pattern:
# i = 0
# j = 3
# for row in range(4):
#     for col in range(7):
#         # if (col == 0 or col == 6 or (col == 5 and row == 2) or (col == 4 and row == 1) or (col == 3 and row == 0) or
#         #         (col == 2 and row == 1) or (col == 1 and row == 2)):
#         if col == 0 or col == 6 or (col == 5 and row == 2) or (col == 4 and row == 1):
#             print("*", end=" ")
#         elif row == i and col == j:
#             print("*", end=" ")
#             i = i + 1
#             j = j - 1
#         else:
#             print(end="  ")
#     print()

