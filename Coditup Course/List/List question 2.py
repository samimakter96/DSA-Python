# Program to count total number of Odd and even numbers in the list.

arr = []
size = int(input("How many Element you want to Enter?"))
for i in range(size):
    val = int(input("Enter number:"))
    arr.append(val)
print(arr)
even = 0
odd = 0
for i in range(size):
    if arr[i] % 2 == 0:
        even = even+1
    else:
        odd = odd+1
print("Total Even=", even, "Total Odd=", odd)