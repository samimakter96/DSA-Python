n = int(input("Enter your number you want to store in the array:"))

a = []
for i in range(1, n+1):
    a.append(i)
print(a)


# Approach 2: using function


def storing_element(m):

    arr = []
    for j in range(1, m+1):
        arr.append(j)
    return arr


x = int(input("Enter number to store element:"))
print(storing_element(x))