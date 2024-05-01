arr = [4, 5, 6, 7, 0, 1, 2, 3]
ans = float('inf')
index = -1
for i in range(len(arr)):
    if arr[i] < ans:
        ans = arr[i]
        index = i
print(index)