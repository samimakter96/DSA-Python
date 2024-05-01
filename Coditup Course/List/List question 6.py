# program to find min number of the list


arr = []
size = int(input("Enter size of the list:"))
for i in range(size):
    val = int(input("Enter number to add in the list:"))
    arr.append(val)
min = arr[0]
for i in range(size):
    if arr[i] < min:
        min = arr[i]
print("Minimum Number=", min)