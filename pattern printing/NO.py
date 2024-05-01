# print NO:

str1 = "NO"
print_N = [[" "for row in range(6)] for col in range(6)]
print_O = [[" "for row in range(6)] for col in range(6)]

# code for N
for row in range(6):
    for col in range(6):
        if col == 0 or col == 5 or row == col:
            print_N[row][col] = "*"

# code for O
for row in range(6):
    for col in range(6):
        if ((row == 0 or row == 5) and (col !=0 and col !=5)) or ((col == 0 or col == 5) and (row !=0 and row !=5)):
            print_O[row][col] = "*"


for row in range(6):
    for col in range(6):
        print(print_N[row][col], end=" ")
    print(end="  ")
    for col in range(6):
        print(print_O[row][col], end=" ")
    print()