# append () = This method is used to append (add) a object at the end of the list
# Example
a = ["ram", "shyam", "sita", "gita"]
a.append("mita")
print(a)

# Program to implement append() method

a = []
for i in range(5):
    x = input("Enter item to add in the list:")
    a.append(x)
print(a)