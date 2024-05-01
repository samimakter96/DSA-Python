# count () = This method id used to count the frequency of a given object

# Example
a = ["ram", "shyam", "ram", "gita", "sita", "ram"]
x = a.count("ram")
print("Frequency of ram is =", x)

# Program to implement count() method

a = []
for i in range(5):
    x = int(input("Enter the number to add in the list:"))
    a.append(x)
x = int(input("Enter the value whose frequency you want:"))
f = a.count(x)
print("frequency of =", f)