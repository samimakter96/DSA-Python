def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]
    print(arr)


nums = [3, 6, 5, 1, 7, 2, 4]
selection_sort(nums)

# Time Complexity: O(N^2)   Space Complexity: O(1)
