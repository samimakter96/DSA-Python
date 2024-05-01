# using for loop: TC - O(N)  SC - O(1)
# n = 5
# sum_ = 0
# for i in range(n+1):
#     sum_ += i
# print(sum_)

# using formula:  TC- O(1)  SC- O(1)
# n = 5
# sum_ = n * (n+1) // 2
# print(sum_)


""" Using Recursion: parameterized way"""


# def func(n, sum_):
#
#     if n < 1:
#         print(sum_)
#         return
#
#     func(n-1, + sum_ + n)
#
#
# n = 5
# func(n, 0)

# Time complexity: O(N)   Space Complexity: O(N)


""" Using Recursion Functional way """


def print_sum_n(n):

    if n == 0:
        return 0
    else:
        return n + print_sum_n(n - 1)


n = 5
result = print_sum_n(n)
print(result)

# Time complexity: O(N)   Space Complexity: O(N)
