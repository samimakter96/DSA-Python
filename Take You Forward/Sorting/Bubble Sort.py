"""
Bubble Sort Algorithm:
1. if the first element (index = 0) is greater than the next element (index = 1) then swap
2. if the current element is lesser than the next element, move to the next element. Repeat step 1
"""


"""Ascending Order"""

arr = [13, 46, 24, 52, 20, 9]
for i in range(len(arr)-1):
    for j in range(len(arr)-1-i):   # i is to avoid unnecessary comparisons for element already sorted at the end.
        if arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
print("arr after sorting in Ascending order:", arr)


"""Descending Order"""
# in descending order if the current element is less than the next element then swap

num = [23, 12, 45, 100, 7, 70, 67]
for i in range(len(num)-1):
    for j in range(len(num)-1-i):
        if num[j] < num[j+1]:
            temp = num[j]
            num[j] = num[j+1]
            num[j+1] = temp
print("arr after sorting in descending order:", num)

# Time Complexity : O(N^2)   Space Complexity: O(1)


lst = [1, 2, ]

