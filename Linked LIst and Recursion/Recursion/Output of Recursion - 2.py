def count(i):

    if i == 5:
        return 0

    else:
        return i + count(i+3)


print(count(1))

""" Q. What will be the output?
    i == 5, its never happen because i gets increase and increase it gets into an infinity loop 
"""