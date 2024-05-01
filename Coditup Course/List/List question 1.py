# Program to find sum of Element of the list.

arr = []
size = int(input("How many element you want to Enter:"))
for i in range(size):
    val = int(input("Enter number:"))
    arr.append(val)
sum = 0
for i in range(size):
    sum = sum + arr[i]
print("sum of List Elements=", sum)