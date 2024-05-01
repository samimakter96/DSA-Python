# Program to find second maximum number in the list

# a = []
# size = int(input("Enter size of the list:"))
# for i in range(size):
#     val = int(input("Enter number:"))
#     a.append(val)
# max_val = max(a)
# print("Maximum value in the List:", max_val)
# a.remove(max_val)
# smax = max(a)
# print("Second Maximum value in the list=",smax)

# Example 2
a = []
size = int(input("Enter size of the list:"))
for i in range(size):
    val = int(input("Enter number"))
    a.append(val)
a.sort()
print("Maximum number=", a[size-1])
print("Second Maximum number=", a[size-2])