# reverse() = This method is used to reverse the elements present in the list

# Syntax: list.reverse()

# Example

arr = [5, "ram", 10, "ravi", 10]
arr.reverse()
print(arr)

# Program to implement reverse() method

arr = []
for i in range(5):
    x = input("Enter item to add in the list:")
    arr.append(x)
print("Original list is:", arr)
arr.reverse()
print("List after reverse is:", arr)
