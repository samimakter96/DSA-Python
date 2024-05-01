# def message():
#     print("Hello python")
#
#
# message()
# message()
# message()
#
# # Q. 1 program to find addition of two numbers using functions
# def add():
#     a = int(input("Enter 1st number:"))
#     b = int(input("Enter 2nd number:"))
#     c = a + b
#     print("Addition =", c)
#
# add()
# add()

# without Argument
# def addition():
#     a = int(input())
#     b = int(input())
#     c = a + b
#     print("Addition=", c)
#
#
# addition()

# def oddeve():
#     a = int(input("Enter number to check:"))
#     if a % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")
#
# oddeve()

# with Arguments
# def addition(a, b):
#     c = a + b
#     print("Addition=", c)
#
#
# x = int(input())
# y = int(input())
# addition(x, y)


# def Oddeve(a):
#     if a % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")
#
#
# n = int(input("Enter number to check:"))
# Oddeve(n)

# Default Argument
def add(a, b, c=5):
    d = a + b + c
    print("Addition=", d)


add(5, 6, 7)
add(5, 10)
