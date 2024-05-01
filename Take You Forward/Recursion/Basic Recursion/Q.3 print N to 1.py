""" print N to 1 using recursion"""


def print_n_one(n, i):

    if n < i:
        return
    print(n)

    return print_n_one(n-1, i)


n = 5
print_n_one(n, 1)


# solution 2:
def print_n_times_reverse(n):
    if n == 0:
        return []
    else:
        # Recursive call to print_n_times_reverse with n-1
        result = print_n_times_reverse(n - 1)
        # Prepend n to the result list
        result = [n] + result
        return result


n = 5
print(print_n_times_reverse(n))


# Approach 3:

def recursive_function(x, ans):

    if x == 0:
        return
    ans.append(x)

    recursive_function(x-1, ans)


def print_nos(x):

    ans = []

    recursive_function(x, ans)

    return ans


x = 5
print(print_nos(x))


# back tracking without using (-)
def print_num(i, n):

    if i > n:
        return
    print_num(i + 1, n)
    print(i)


n = 5
print_num(1, n)