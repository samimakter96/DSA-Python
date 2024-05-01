""" Write a program to create a class count_objects
and calculate the number of objects that has been created in realtime."""


class Count_objects:

    i = 0   # static variable

    def __init__(self):
        Count_objects.i = Count_objects.i + 1   # Access static variable using class name and increment by 1


def main():
    a = Count_objects()
    b = Count_objects()
    c = Count_objects()
    print(Count_objects.i)
    d = Count_objects()
    print(Count_objects.i)
    e = Count_objects()
    print(Count_objects.i)


main()