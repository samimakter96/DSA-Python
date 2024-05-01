# program to count frequency of a given number

arr = []
size = int(input("Enter size of the list:"))
for i in range(size):
    val = int(input("Enter number:"))
    arr.append(val)
key = int(input("Enter number to find frequency:"))
count = 0
for i in range(size):
    if arr[i] == key:
        count = count+1
print("Frequency=", count)