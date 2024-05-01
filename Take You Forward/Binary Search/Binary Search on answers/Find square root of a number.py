def search_square_root(n):

    low = 1
    high = n
    ans = 0

    while low <= high:
        mid = (low + high) // 2
        if mid * mid <= n:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1

    return ans


n = 36
print(search_square_root(n))

# Note: we can return high also without using extra ans variable

# Time Complexity: O(LogN)  Space Complexity; O(1)
