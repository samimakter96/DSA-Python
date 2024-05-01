def count(i):

    if i == 6:
        return

    else:
        count(i+1)
        print(i)


count(1)


""" Q. What will be the output?
    
    first it increment the i and then it print(i)
    if i not equal 6 then it increment i when it match i == 6 then it print(i) in reverse order 5 4 3 2 1  
"""