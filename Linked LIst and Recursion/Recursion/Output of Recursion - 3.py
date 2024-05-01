def count(i):

    if i == 6:
        return
    else:
        print(i)
        count(i+1)


count(1)


""" Q. what will be the output?
    if the base condition not match it first print i and then increment i
    if i not equal 6 then it print (i) 1 2 3 4 5 when the base condition match i == 6 then it return  
"""