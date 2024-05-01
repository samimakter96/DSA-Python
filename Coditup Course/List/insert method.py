# insert() = This method is used to insert an object/value at the given index

# Syntax: list.insert(index,object)

# Example

a = [5, "samim", 10]
a.insert(2, "akter")
print(a)

# Program to implement insert() method

a = []
for i in range(3):
    x = input("Enter value:")
    a.append(x)
print("Original list is", a)
index = int(input("Enter index where you want to insert:"))
value = input("Enter value to insert:")
a.insert(index, value)
print("List after insertion:", a)