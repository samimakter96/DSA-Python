# Types of function :-
""" 1. Built-in function: len, type, print, del, list, dict, int, float...."""

# In build function : Here print() and lent() is in build function
# print("This is function")
# print(len("something"))

# 2. User defined function: (we create to fulfil our business requirements):
""" syntax to define function:
def function_name(parameter1, parameter2):
    "body"
    "body"
    "body"
    return value 

function_name()  # function call    
"""

def calculator(a,b):
    print("addition:", a + b)
    print("subtraction", a - b)
    print("multiplication", a * b)
    print("division", a / b)


calculator(8, 4)
calculator(5, 10)
calculator(6, 8)

""" positional arguments: 
1. order should be maintain  2. no. of parameter = no. of arguments"""
def greet(first_name, last_name):
    print("good evening", first_name, last_name)


greet("samim", "akter")

""" keyword arguments:
1.order is important  2. no. of parameter = no. of arguments  3. keyword arguments should follow positional arguments"""

def greet(first_name, last_name):
    print("good evening", first_name, last_name)


greet(last_name="samim", first_name="akter")
greet("samim", last_name="akter")
# print(last_name="samim", "akter")   # SyntaxError: positional argument follows keyword argument

""" default argument:
1. order is important  2. no. of parameter may or may not be equal no. of arguments"""

def greet(first_name="guest"):
    print("good evening", first_name)


greet("Samim")

""" variable length arguments: """

def test(*args):
    print(args)
    print(len(args))
    print(type(args))


test("India", "Bangladesh", "Pakistan")

def test(**kwargs):
    print(kwargs)
    print(len(kwargs))
    print(type(kwargs))


test(county="India", firstname="rohit")


def fun(name, * fav_subjects):
    print(name, "likes to read")
    for subjects in fav_subjects:
        print(subjects)


fun("samim", "python", "Geography", "Maps")