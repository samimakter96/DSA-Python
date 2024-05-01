def minimum_rotated_array(arr):
    low = 0
    high = len(arr) - 1
    ans = float('inf')

    while low <= high:
        mid = (low + high) // 2

        if arr[low] <= arr[mid]:  # if left part is sorted
            ans = min(ans, arr[low])  # keep the minimum
            low = mid + 1  # eliminate left half

        else:  # if right part is sorted
            ans = min(ans, arr[mid])  # keep the minimum
            high = mid - 1  # eliminate right half

    return ans


arr = [3, 4, 5, 1, 2]
print(minimum_rotated_array(arr))