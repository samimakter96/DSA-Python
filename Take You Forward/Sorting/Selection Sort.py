"""
Selection Sort Algorithm:
1. search for the Smallest element in the list of numbers
2. swap Smallest number with the 0th index element.
3. take the sub-list (ignore sorted part) and repeat step 1 and 2 un-till all the element are sorted.
"""

"""Ascending Order"""
# list1 = [56, 3, 2, 78, 6, 0]
# min_val = min(list1)    # search min value
# min_ind = list1.index(min_val)   # search in which index min value is present
# # swap min_val with the 0 th index
# temp = list1[0]
# list1[0] = list1[min_ind]
# list1[min_ind] = temp
# print(list1)    # this is the first iteration we have to do this again and again un till all the element are sorted

list1 = [56, 3, 2, 78, 6, 0]
for i in range(len(list1)):
    min_val = min(list1[i:])    # min value start from i to n value
    min_ind = list1.index(min_val, i)   # if there is any duplicates value
    list1[i], list1[min_ind] = list1[min_ind], list1[i]   # swap
print(list1)


# without using Built in min() function
arr = [56, 3, 2, 78, 6, 0]
for i in range(len(arr)):
    minimum = i
    for j in range(i, len(arr)):
        if arr[j] < arr[minimum]:
            minimum = j
    temp = arr[minimum]
    arr[minimum] = arr[i]
    arr[i] = temp
print("array after selection sort:", arr)


"""Descending Order"""
# in descending order everything is same, just instead of min we find max value.

num = [5, 15, 3, 17, 15, 5, 0]
for i in range(len(num)):
    max_val = max(num[i:])
    max_ind = num.index(max_val, i)  # if there is any duplicate value that is why we use i here if i = 0 max_index = 0
    temp = num[i]
    num[i] = num[max_ind]
    num[max_ind] = temp
print("Selection sort after sorting in descending order:", num)

# Without using Built in max() function
num = [5, 15, 3, 17, 15, 5, 0]
for i in range(len(num)-1):
    maximum = i
    for j in range(i, len(num)):
        if num[j] > num[maximum]:
            maximum = j
    temp = num[maximum]
    num[maximum] = num[i]
    num[i] = temp
print("sorting in descending order:", num)


# Time Complexity --> O(N^2)    Space Complexity --> O(1)