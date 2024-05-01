# Linear Search: Time Complexity: O(N)  Space Complexity: O(1)

def first_and_last(arr, n, k):
    first = -1
    last = -1
    for i in range(n):
        if arr[i] == k:
            if first == -1:
                first = i
            last = i
    return first, last


arr = [2, 4, 6, 8, 8, 8, 11, 13]
k = 8
n = len(arr)

ans = first_and_last(arr, n, k)
print(ans[0], ans[1])