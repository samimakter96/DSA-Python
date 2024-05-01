"""
what is flor: The floor of x is the largest element in the array which is smaller than or equal to x( i.e. largest
element in the array <= x).
"""


def find_flor(arr, n, x):

    low = 0
    high = n - 1
    ans = -1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] <= x:
            ans = arr[mid]
            # look for smaller index on the left
            low = mid + 1
        else:
            high = mid - 1  # look on the right

    return ans

"""
what is ceil: The ceiling of x is the smallest element in the array greater than or equal to x( i.e. smallest element 
in the array >= x).
"""


def find_ceil(arr, n, x):

    low = 0
    high = n - 1
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= x:
            ans = arr[mid]
            # look for smaller on the left
            high = mid - 1
        else:
            low = mid + 1   # look on the right
    return ans


def get_flor_and_ceil(arr, n, x):
    f = find_flor(arr, n, x)
    c = find_ceil(arr, n, x)
    return f, c


arr = [3, 4, 4, 7, 8, 10]
n = 6   # length
x = 5   # target

ans = get_flor_and_ceil(arr, n, x)
print("The floor and ceil are:", ans[0], ans[1])