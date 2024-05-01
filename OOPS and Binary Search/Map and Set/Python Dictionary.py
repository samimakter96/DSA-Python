"""
A Dictionary in python is a collection of key values, used to store data value like a map.
Dictionary Syntax: --> dict_var = {key1: value1, key2: value2,....}
"""

# Dictionary Syntax: --> dict_var = {key1: value1, key2: value2,....}
Dict = {1: "Geeks", 2: "For", 3: "Geeks"}
print(Dict)

# Creating a Dictionary in python
Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print("\nDictionary with the use of Integer Keys:")
print(Dict)

Dict = {'Name': 'Samim', 1: [1, 2, 3, 4]}
print("\nDictionary with the use of string and integer Mixed Keys:")
print(Dict)

# Different ways to create python Dictionary
Dict = {}
print("Empty Dictionary")
print(Dict)

Dict = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'})
print("\nDictionary with the use of dict():")
print(Dict)

Dict = dict([(1, 'Geeks'), (2, 'For'), (3, 'Geeks')])
print("\nDictionary with each item as a pair:")
print(Dict)

# Nested Dictionary
Dict = {1: 'Geeks', 2: 'For', 3: {'A': 'Welcome', 'B': 'To', 'C': 'Geeks'}}
print(Dict)

# Adding elements to a Dictionary
Dict = {}
print("Empty Dictionary:")
print(Dict)
Dict[0] = "Samim"
Dict[2] = "Programmer"
Dict[3] = 5
print("\nDictionary after adding 3 elements:")
print(Dict)

Dict['add_element'] = 2, 3, 4
print("\nDictionary after adding 3 elements:")
print(Dict)
# update
Dict[2] = 'Welcome'
print("\nUpdate key value:")
print(Dict)

Dict[5] = {'Nested': {'1': 'Life', '2': 'Geeks'}}
print("\nAdding a Nested key:")
print(Dict)

# Accessing elements of a Dictionary
Dict = {1: 'Programmer', 'name': 'Samim', 3: 'Geeks'}
print("Accessing a element using key:")
print(Dict['name'])
print("Accessing a element using key:")
print(Dict[1])

# get() --> accessing the element from a dictionary. this method accepts key as a argument and returns the value.
Dict = {1: 'Programmer', 'name': 'Samim', 3: 'Geeks'}
print("Accessing a element using get:")
print(Dict.get('name'))
print(Dict.get(1))

# Accessing an element of a nested Dictionary
Dict = {'Dict1': {1: 'Geeks'}, 'Dict2': {'Name': 'Samim'}, 'Dict3': {'love': 'Coding'}}
print(Dict['Dict1'])
print(Dict['Dict1'][1])
print(Dict['Dict2']['Name'])

# Deleting Elements using del keyword
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
print(Dict)
del(Dict[1])
print("Data after deletion Dictionary")
print(Dict)

# Traverse through a dictionary


def traverse_dic(dic):
    for key in dic:
        print(key, dic[key])    # dic[key] = key value


my_dic = {'name': 'samim', 1: 'Geeks', 'love': 'programming'}
traverse_dic(my_dic)

# Search an element in a Dictionary


def search_dic(dic, value):
    for key in dic:
        if dic[key] == value:
            return key, value


my_dic = {'name': 'samim', 1: 'Geeks', 'love': 'programming'}
print(search_dic(my_dic, 'samim'))

# How to find frequency of element using dictionary
arr = [2, 2, 3, 4, 1, 3, 2, 1, 4, 5, 6, 8, 2]
frequency = {}

for item in arr:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1

print(frequency)

# Approach 2:
frequency = {}
for key in arr:
    frequency[key] = frequency.get(key, 0) + 1
print(frequency)

# How to build hash map / dictionary using it's index
nums = [2, 5, 6, 7, 3]
frequency_map = {}
for i in range(len(nums)):
    frequency_map[nums[i]] = i
print(frequency_map)