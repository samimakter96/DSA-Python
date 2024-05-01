# # 24. X pattern:
# i = 0
# j = 4
# for row in range(5):
#     for col in range(5):
#         if row == i and col == j:
#             print("*", end=" ")
#             i = i + 1
#             j = j - 1
#         elif row == col:
#             print("*", end=" ")
#         else:
#             print(end="  ")
#     print()

# 25. Y pattern:
# for row in range(5):
#     for col in range(5):
#         if (col == 2 and row > 1) or (row == col and col < 2) or (row == 0 and col == 4) or (row == 1 and col == 3):
#             print("*", end=" ")
#         else:
#             print(end="  ")
#     print()

# 26. Z pattern:
i = 1
j = 4
for row in range(6):
    for col in range(6):
        if row == 0 or row == 5:
            print("*", end=" ")
        elif row == i and col == j:
            print("*", end=" ")
            i = i + 1
            j = j - 1
        else:
            print(end="  ")
    print()