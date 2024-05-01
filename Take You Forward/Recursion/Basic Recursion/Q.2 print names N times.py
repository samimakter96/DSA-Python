# Q.1 print names N times using recursion

def print_names(i, n):

    if i > n:
        return
    print(num)

    return print_names(i+1, n)


num = "samim"
n = 5

result = print_names(1, n)


# Solution 2:

def print_names(n):
    # Base case: stop recursion when n becomes 0
    if n == 0:
        return []
    else:
        # Recursive call to print N times with n-1
        result = print_names(n - 1)
        # Append "samim" to the result list
        result.append("samim")
        return result


n = 5
print(print_names(n))
