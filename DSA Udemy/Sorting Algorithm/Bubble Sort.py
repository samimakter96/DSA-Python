def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print(arr)


nums = [2, 7, 3, 1, 5, 4, 6]
bubble_sort(nums)

# Time Complexity: O(N^2)   Space Complexity: O(1)
