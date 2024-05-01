# program to find max number of the list

a = []
size = int(input("Enter size of the list:"))
for i in range(size):
    val = int(input("Enter number to add list:"))
    a.append(val)
max = a[0]
for i in range(size):
    if a[i] > max:
        max = a[i]
print("Maximum number=", max)