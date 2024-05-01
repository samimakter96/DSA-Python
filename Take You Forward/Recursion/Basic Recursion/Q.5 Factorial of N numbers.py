# using for loop

# n = 5
# fact = 1
# for i in range(1, n+1):
#     fact = fact * i
# print("factorial of n is:", fact)


# factorial using Recursion

def fact(n):

    if n == 0 or n == 1:
        return 1

    return n * fact(n-1)


n = 5
factorial = fact(n)
print(factorial)

# TC : O(N)   SC : O(N)


# factorial Number Not Greater than N

n = 7
fact = 1
res = []
if n == 1:
    res.append(1)
else:
    for i in range(1, n+1):
        fact *= i
        if fact < n:
            res.append(fact)
print(res)