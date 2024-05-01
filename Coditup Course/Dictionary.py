"""Dictionary is a collection which is ordered and changeable. no duplicates member."""

dict1 = {'brand': 'suzuki', 'model': 'Alto', 'year': 2020}
print(dict1)

"""Accessing items"""
# you can access the items of a dictionary by referring to its key name, inside square brackets

x = dict1['model']
print(x)
a = dict1['brand']
print(a)

# there is also a method called get() for the same task
y = dict1.get('model')
print(y)
z = dict1.get('brand')
print(z)

"""Loop through a dictionary"""

dict1 = {'brand': 'suzuki', 'model': 'Alto', 'year': 2020}
print(dict1)

for x in dict1:
    print(x)    # this will print key only

# for x in dict1.keys():
#     print(x)

# or
for x in dict1:
    print(dict1[x])   # this will print the values only


# for x in dict1.values():
#     print(x)

# items() --> it will print the values in the dictionary along with keys
for x, y in dict1.items():
    print(x, y)

"""change value"""
# you can change the value of a specific items by referring to its key name
# update
dict1 = {'brand': 'suzuki', 'model': 'Alto', 'year': 2020}
print(dict1)
dict1['year'] = 2024
print(dict1)
dict1['model'] = 'maruti'
print(dict1)

# Checking whether a key exists in the Dictionary

dict1 = {'brand': 'suzuki', 'model': 'Alto', 'year': 2020}
if 'model' in dict1:
    print("yes, 'model' is one of the keys in the dictionary")
else:
    print("NO, 'model' is not one of the key in the dictionary.")


# Adding new element in the dictionary
dict1 = {'brand': 'suzuki', 'model': 'Alto', 'year': 2020}
print(dict1)
dict1['color'] = 'white'
print(dict1)

# len() function --> this function is used to find length of the dictionary
dict1 = {'brand': 'suzuki', 'model': 'Alto', 'year': 2020}
x = len(dict1)
print("Length of the Dictionary =", x)

# pop() --> this method removes the element with specified key name
dict1 = {'brand': 'suzuki', 'model': 'Alto', 'year': 2020}
print(dict1)
dict1.pop('model')
print(dict1)

# popitem() --> this method removes the last element of the dictionary
dict1 = {'brand': 'suzuki', 'model': 'Alto', 'year': 2020}
print(dict1)
dict1.popitem()
print(dict1)

# del keyword --> this keyword removes the item with specified key name
dict1 = {'brand': 'suzuki', 'model': 'Alto', 'year': 2020}
print(dict1)
del dict1['year']
print(dict1)
# del dict1
# print("delete whole dictionary", dict1) # after deleting all the element is shows error because dict doesnt exits 

# clear()
dict1 = {'brand': 'suzuki', 'model': 'Alto', 'year': 2020}
print(dict1)
dict1.clear()
print(dict1)

# copy() --> it will print the values in the dictionary along with keys.
dict1 = {'brand': 'suzuki', 'model': 'Alto', 'year': 2020}
x = dict1.copy()
print(x)

# fromkeys() --> returns a dictionary with the specified keys and the specified value.
x = ('first key', 'second key', 'third key')
y = 0
dict1 = dict1.fromkeys(x, y)
print(dict1)

# setdefault() --> returns the value of the item with the specified key.
#              --> if the key does not exist, it inserts the key, with the specified value
dict1 = {'brand': 'suzuki', 'model': 'Alto', 'year': 2020}
x = dict1.setdefault("brand", "Toyota")
print(x)    # since "brand" key is already present sot it will return the value of this key. suzuki

dict1 = {'brand': 'suzuki', 'model': 'Alto', 'year': 2020}
x = dict1.setdefault("place", "New Delhi")
print(x)    # since place key is not present in the dict1 so it will insert the key value and print New Delhi.
print(dict1)


# update() --> inserts the specified items to the dictionary
dict1 = {'brand': 'suzuki', 'model': 'Alto', 'year': 2020}
dict1.update({"location": "saket"})
print(dict1)


"""Write a program to store students information like Admission number, Roll no, Name and marks in a dictionary 
and display information on the basis of Admission number"""

students_DB = {}
# ask input from user or 'q' to exit
while True:
    line = input("Please input the ID and name separated by comma or q to exit:")
    if line == 'q':
        break
    id, name = line.split(',')
    students_DB.update({id: name})
# output
for x, y in students_DB.items():
    print(x, y)

# searching a key
key = input("Enter ID to search:")
if key in students_DB:
    print('key=', key, 'value=', students_DB[key])
else:
    print("key not found")