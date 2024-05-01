
"""
Approach:
1. Select an element in each iteration from the unsorted array(using a loop).
2. Place it in its corresponding position in the sorted part and shift the remaining elements accordingly
(using an inner loop and swapping).
3. The “inner while loop” basically shifts the elements using swapping.
"""
arr = [13, 46, 24, 52, 20, 9]
for i in range(1, len(arr)):
    j = i
    while j > 0 and arr[j-1] > arr[j]:
        temp = arr[j]
        arr[j] = arr[j-1]
        arr[j-1] = temp
        j = j - 1
print(arr)


# Approach 2:
arr = [10, 4, 25, 1, 5]
for i in range(1, len(arr)):
    current_element = arr[i]
    pos = i
    while pos > 0 and current_element < arr[pos-1]:
        arr[pos] = arr[pos-1]
        pos = pos - 1
    arr[pos] = current_element
print(arr)