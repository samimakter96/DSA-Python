""" Once a tuple is created, you cannot change its values because tuples are unchangeable, or immutable"""

# Creating empty tuple
tuple1 = ()
print(type(tuple1))

tuple1 = tuple()
print(type(tuple1))

# Creating single element tuple
tup = (2)   # this is not a tuple it's a int
print(type(tup))

tup1 = (2,)   # this will be a tuple class. i have to give comma(,)
print(type(tup1))

# Creating tuple from existing sequences
t = tuple("word")
print(t)

# Creating tuple from list
list1 = [1, 2, 3, 4, 5]
tuple3 = tuple(list1)
print(tuple3)

# Traversing tuple
tup1 = (1, 2, 3, 4, 5)
for i in tup1:
    print(i)

# for i in range(tup1):
#     print(tup1[i])

# Joining tuple:
tup1 = (1, 2, 3, 4)
tup2 = (6, 7, 8)
tup3 = tup1 + tup2
print(tup3)

# Repeating or Replication tuples
tup = (1, 2, 3)
tup2 = tup * 3
print(tup2)

# Slicing the tuple
# syntax: [start:stop:step]

tuple1 = (10, 11, 12, 13, 14, 15)
tuple2 = tuple1[3:5]    # by default the step value is 1
print(tuple2)
tuple3 = tuple1[0:5:2]
print(tuple3)

# len() method --> this method returns length of the tuple
tup = ("samim", "Ram", 101, 10.5, "True")
print(len(tup))

# max() method
a = (10, 20, 50, 30, 100)
print(max(a))
# min()
print(min(a))

# index() --> it return the index of an existing element in the tuple
a = (1, 4, 6, 10, 3, 20)
print(a.index(10))

# count() --> return the frequency of given element.
a = (10, 20, 3, 10, 50, 10, 40)
print(a.count(10))

# create empty tuple
t = tuple()
print(t)
# create tuple from a list
t = tuple([1, 2, 3])
print(t)
# creating tuple from string
tuple1 = tuple("xyz")
print(tuple1)
# creating tuple from key of dictionary
tuple1 = tuple({1: 'm', 2: 'n'})
print(tuple1)

# tuple is unchangeable or immutable
# but there is another way to achieve this. you can convert the tuple into a list. change the list, and convert the list
# back into a tuple

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

# check if item exits
# in operator
tuple1 = ("ram", "shyam", "sita", "gita")
if "ram" in tuple1:
    print("yes, element present in the tuple")
else:
    print("No, element is not present in the tuple")

# Add items
# Once a tuple is created, you cannot add items to it, tuple are unchangeable
# you cannot add items to a tuple

# Delete tuple element
# Removing individual elements of the tuple is not possible. to remove entire tuple, just use the del statement.
tuple1 = (1, 2, 3, 4)
print(tuple1)
del(tuple1)
print('after deleting tuple')
# print(tuple1) ---> error