# program to reverse the list itself

arr = []
size = int(input("Enter size of the list:"))
for i in range(size):
    val = int(input("Enter number:"))
    arr.append(val)

print("Given List:", arr)

left = 0
right = len(arr)-1

while left < right:
    temp = arr[left]
    arr[left] = arr[right]
    arr[right] = temp
    left = left + 1
    right = right - 1

print("List after reverse=")
for i in range(size):
    print(arr[i])