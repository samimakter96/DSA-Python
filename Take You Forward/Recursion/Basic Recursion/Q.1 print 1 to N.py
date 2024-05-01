
""" print 1 to N using recursion """


def print_n_times(i, n):
    # Base condition
    if i > n:
        return

    print(i)
    # recursive call
    return print_n_times(i+1, n)


n = 5
print_n_times(1, n)

# Approach 2:


def print_n_times(n):

    if n == 0:
        return
    print_n_times(n - 1)
    print(n)


n = 5
print_n_times(n)



# Solution 2:

"""
You are given an integer ‘n’.

Your task is to return an array containing integers from 1 to ‘n’ (in increasing order) without using loops.
"""


def print_n_times(n):
    # Base case: stop recursion when n becomes 0
    if n == 0:
        return []
    else:
        # Recursive call to printNos with n-1
        result = print_n_times(n - 1)
        # Append n to the result list
        result.append(n)
        return result


n = 5
print(print_n_times(n))


# back tracking without using (+)

def print_num(i, n):

    if i < 1:
        return
    print_num(i - 1, n)
    print(i)


n = 5
print_num(n, n)
