# remove() = This method is used to delete an object/value from the given list. Note that it delete the first occurrence
# of the list.

# Syntax: list.remove(object)

# Example

a = [5, "ram", 10, "ravi", 10]
a.remove(10)
print(a)

# Program to implement remove method

a = []
for i in range(5):
    x = input("Enter value:")
    a.append(x)
print("Original list is:",a)
val = input("Enter the value to remove:")
a.remove(val)
print("List after deletion =", a)