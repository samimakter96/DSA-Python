def insertion_sort(arr):
    for i in range(1, len(arr)):
        curr_element = arr[i]
        pos = i
        while curr_element < arr[pos-1] and pos > 0:
            arr[pos] = arr[pos - 1]
            pos -= 1
        arr[pos] = curr_element
    print(arr)


nums = [5, 7, 3, 4, 1, 2, 6]
insertion_sort(nums)

# Time Complexity: O(N^2)   Space Complexity: O(1)
