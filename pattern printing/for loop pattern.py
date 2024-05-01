# 1. increasing triangle pattern

for i in range(1,6,+1):
    string = ""
    for j in range(1,i+1):
        string = string+"*"
    print(string)

# 2. decreasing triangle
for i in range(1, 6, +1):
    string = ""
    for j in range(1, 7-i,1):
        string = string+"*"
    print(string)

# 3. Right sided triangle pattern
for i in range(1, 6, +1):
    string = ""
    for j in range(1, 6-i,1):
        string = string+"  "
    for j in range(1, i+1,1):
        string = string+" * "
    print(string)

# 2. right sided triangle.
for i in range(1, 6, +1):
    string = ""
    for j in range(1,i+1,1):
        string = string+"   "
    for j in range(1, 7-i,1):
        string = string+" * "
    print(string)

# Hill pattern
for i in range(1, 6,+1):
    string = ""
    for j in range(1, 7 - i, 1):
        string = string+" "
    for j in range(1, i + 1):
        string = string+"*"
    for j in range(2, i+1):
        string = string+"*"

    print(string)

# Reverse Hill pattern
for i in range(1, 6, +1):
    string = " "
    for j in range(1, i + 1):
        string = string+"   "
    for j in range(2, 7 - i, 1):
         string = string+" * "
    for j in range(1, 7 - i, 1):
         string = string+" * "
    print(string)