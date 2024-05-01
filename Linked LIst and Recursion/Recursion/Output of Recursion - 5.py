def count(i):

    if i == 6:
        return

    else:
        print(i)
        count(i+1)
        print(i)


count(1)


""" Q. What will be the output?
    
    if the base condition is not match then it print(i), and then increment i , when i == 6 then it return and print(i)
    in reverse order like 5 4 3 2 1
    
    so, the output will be 1 2 3 4 5 5 4 3 2 1
"""