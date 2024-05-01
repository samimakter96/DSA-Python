# index () = This method is used to find the index of the element

# Syntax: list.index(object)

# Example

a = ["ram", "shyam", "ram", "gita"]
x = a.index("ram")
print("index of the ram =", x)


# Program to implement index() method

a = []
for i in range(5):
    x = input("Enter value:")
    a.append(x)
x = input("Enter value to find index:")
z = a.index(x)
print("index of =", z)