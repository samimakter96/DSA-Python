"""
A set in python programming is an unordered collection data type that is iterable, mutable and has no duplicate elements
Set are represented by { } (values enclosed in curly braces)
Since sets are unordered, we cannot access items using indexes as we do in lists.
"""

# Example:
var = {"samim", "love", "programming"}
print(type(var))

my_set = {"a", "b", "c"}
print(my_set)
# Add element to the set. set is a mutable We can only add or delete items in the set.
my_set.add("d")
# set is an unordered datatype. which means we cannot know in which order the element of the set are stored
print(my_set)

# a set cannot have a duplicate values. Every item in it is a unique value.
my_set = {"Geeks", "for", "Geeks"}
print(my_set)   # you can see only one "Geeks" are print because sets cannot have duplicate

# once it is created we cannot change its value.
# my_set[1] = "Hello"
# print(my_set) --> TypeError: 'set' object does not support item assignment

# Heterogeneous Element with Python Set --> set can store a mixture of string, integer, boolean, etc
my_set = {"Geeks", "for", 10, True, 25.5}
print(my_set)

# Adding elements to python Sets
people = {"Jay", "Ankit", "Archi"}
print("People:", people)

people.add("Samim")
print("People:", people)

# adding elements to the set using iterator
for i in range(1, 6):
    people.add(i)
print("\nSet after adding element:", end=" ")
print(people)

# Union() --> two sets can be merged using union() function or | operator.
people = {"Jay", "Samim", "Archi"}
vampires = {"Karan", "Arjun"}
dracula = {"Ankit", "Raju"}
# Union using union() function
population = people.union(vampires)
print(population)
# Union using "|" operator
population = people | dracula
print(population)


# remove duplicates using set

my_list = [1, 2, 2, 3, 1, 4, 3, 5, 4, 1]

unique_element = []
seen = set()

for element in my_list:
    if element not in seen:
        unique_element.append(element)
        seen.add(element)

print("after removing duplicates:", unique_element)