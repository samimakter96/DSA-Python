arr = [1, 4, 7, 8, 10]
n = 5
x = 7

low = 0
high = n - 1
ans = n

while low <= high:
    mid = (low + high) // 2
    if arr[mid] > x:
        ans = mid
        high = mid - 1
    else:
        low = mid + 1
print(ans)