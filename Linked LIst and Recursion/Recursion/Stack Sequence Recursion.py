def count(i):
    if i > 5:
        # Print the elements inside the stack from top to bottom
        return 0
    
    else:
        print(i, end=" ")
        count(i + 1)


# calling the function count
count(1)
