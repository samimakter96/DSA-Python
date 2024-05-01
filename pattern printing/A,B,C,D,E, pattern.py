# 1. A pattern
# for row in range(7):
#     for col in range(5):
#         if ((col == 0 or col == 4) and row != 0) or ((row == 0 or row == 3) and (col > 0 and col < 4)):
#             print("*", end="")
#         else:
#             print(end=" ")
#     print()

# 2. B pattern
# for row in range(7):
#     for col in range(5):
#         if(col == 0 or col == 4) or ((row == 0 or row == 3 or row == 6) and (col > 0 and col < 4)):
#             print("*",end=" ")
#         else:
#             print(end="  ")
#     print()

# 3. C Pattern
# for row in range(7):
#     for col in range(5):
#         if (col == 0) or ((row == 0 or row == 6) and (col > 0)):
#             print("*", end=" ")
#         else:
#             print(end=" ")
#     print()
# Modified C Pattern:
# for row in range(7):
#     for col in range(5):
#         if (col == 0 and (row != 0 and row != 6)) or ((row == 0 or row == 6) and (col > 0)):
#             print("*", end=" ")
#         else:
#             print(end=" ")
#     print()

# 4. D pattern
# for row in range(7):
#     for col in range(5):
#         if(col == 0) or ((col == 4 and(row != 0 and row != 6)) or ((row == 0 or row == 6) and (col > 0 and col < 4))):
#             print("*", end=" ")
#         else:
#             print(end="  ")
#     print()

# 5. E pattern
for row in range(7):
    for col in range(5):
        if (col == 0) or ((row == 0 or row == 3 or row == 6) and (col > 0)):
            print("*", end=" ")
        else:
            print(end="  ")
    print()


