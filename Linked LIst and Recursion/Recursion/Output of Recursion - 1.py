def count(i):

    if i > 5:
        return 0

    else:
        return i * count(i+1)


print(count(1))

""" Q. what will be the output?

    when i > 5 it returns 0 and 6 * 0 = 0, 0 * 5 = 0, 0 * 4 = 0, 0 * 3 = 0, 0 * 2 = 0, 0 * 1 = 0 so, the answer is zero
    anything multiplied by 0 is 0
"""