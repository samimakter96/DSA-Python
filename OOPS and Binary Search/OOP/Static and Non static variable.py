"""How to Create Static variable in python"""

# Creating a blueprint (class) for lego blocks


class Lego:

    # Declare the static variables
    width = 5   # static variable
    height = 5  # static variable

    # Declaring a constructor, taking length and colour as a parameter
    # Remember 'self'(object) is passed to each method
    def __init__(self, length, colour):
        self.length = length    # instance variable
        self.colour = colour      # instance variable
        print('Block of ' + colour + ' colour is manufactured.')


# Creating a lego block (object) of class Lego
block1 = Lego(10, "Red")
block2 = Lego(5, "Blue")

# there are other methods also to create static variable

"""How to Access Static Variables in Python?"""
# Method 1: using class name


class Lego:

    width = 5
    height = 5

    def __init__(self, length, colour):
        self.length = length
        self.colour = colour
        print(f"Length of the block is {length} and the colour is {colour}")

    # Creating a method to access static variables inside class
    def print_static(self):
        print("The Static values are: width =", Lego.width, "and height =", Lego.height)


# Creating a lego block (object) of class Lego
block3 = Lego(10, "Red")
block4 = Lego(5, "Blue")
# calling static variable in main method using ClassName
print(Lego.width)
print(Lego.height)
# Calling the method to display access of static variables
block3.print_static()
block4.print_static()

# Method 2: using object name
# Calling the static variables using instances-
print(block3.width)
print(block4.height)
block3.width = 10   # Accessing static variable through instance, to change its value
print("width of block3 =", block3.width)
print("width of block 4 =", block4.width)
print("width of blocks =", Lego.width)

# Method 3: using the __class_method
# syntax: objectName.__class__.staticVariableName

# calling the static variables using __class__ method-
print('Width of blocks: ', block1.__class__.width)
print('height of blocks:', block1.__class__.height)
# Note the importance of dot operator.

# Method 4: Using the type() method
print('width of blocks:', type(block1).width)
print('height of blocks:', type(block1).height)


"""Static variable example"""


class Bakery:

    type = 'cake'   # class / static variable

    def __init__(self, flavor, price):
        self.flavor = flavor    # non static / instance variable
        self.price = price      # non static / instance variable


# Objects of Bakery class
a = Bakery('Butterscotch cake', 300)
b = Bakery('chocolate-Truffle cake', 250)

print(a.type)   # prints 'cake'
print(b.type)   # prints 'cake'
print(a.flavor)
print(b.flavor)
print(a.price)
print(b.price)

# a, b type same = 'cake' (static) but a, b flavor and price are different (Non-static)
