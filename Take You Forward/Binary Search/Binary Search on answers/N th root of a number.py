

def func(mid, n, m):
    ans = 1
    for i in range(1, n+1):
        ans *= mid
        if ans > m:
            return 2
    if ans == m:
        return 1
    return 0


def binary_search(m):

    low = 1
    high = m
    ans = 1

    while low <= high:
        mid = (low + high) // 2
        mid_n = func(mid, n, m)
        if mid_n == 1:
            return mid
        elif mid_n == 0:
            low = mid + 1
        else:
            high = mid - 1
    return -1


n = 3
m = 27

print(binary_search(m))