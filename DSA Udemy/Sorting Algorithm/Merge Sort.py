def sort_array(arr):

    # step - 1: Dividing
    def merge_sort(arr):
        if len(arr) > 1:    # Base Case
            mid = len(arr) // 2
            left_arr = arr[:mid]
            right_arr = arr[mid:]
            merge_sort(left_arr)
            merge_sort(right_arr)

            # Step-2: Merging
            i = 0
            j = 0
            k = 0
            while i < len(left_arr) and j < len(right_arr):
                if left_arr[i] < right_arr[j]:
                    arr[k] = left_arr[i]
                    i += 1
                    k += 1
                else:
                    arr[k] = right_arr[j]
                    j += 1
                    k += 1

            # Step-3: if any values are left
            while i < len(left_arr):
                arr[k] = left_arr[i]
                i += 1
                k += 1

            while j < len(right_arr):
                arr[k] = right_arr[j]
                j += 1
                k += 1

    merge_sort(arr)
    return arr


nums = [5, 3, 1, 7, 2, 6]
print(sort_array(nums))

# Time Complexity: O(NLogN)   Space Complexity: O(N)
