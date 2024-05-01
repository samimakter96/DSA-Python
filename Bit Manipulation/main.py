arr = [1, -1, 3, 2, -7, -5, 11, 6]

left = 0
right = len(arr) - 1

while left < right:
    if arr[left] < 0:
        arr[left], arr[right] = arr[right], arr[left]
        right -= 1
    else:
        left += 1
print(arr)