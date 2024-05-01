# Find the elements that appears more than N/3 times in the array


# Brute Force Approach:
# arr = [11, 33, 33, 11, 33, 11]
#
# n = len(arr)
# ls = []  # list of answer
#
# for i in range(n):
#     # selected element is arr[i] checking if arr[i] is not already a part of answer
#     if len(ls) == 0 or ls[0] != arr[i]:
#         count = 0
#         for j in range(n):
#             # counting the frequency of arr[i]
#             if arr[j] == arr[i]:
#                 count += 1
#
#         if count > (n//3):
#             ls.append(arr[i])
#
#     if len(ls) == 2:
#         break
#
# print(ls)

# Time Complexity: O(N^2)  Space Complexity: O(N)


# Better Approach:
# from collections import Counter
#
#
# def majority_element(arr):
#
#     n = len(arr)
#     # Count the occurrences of each element using Counter
#     count = Counter(arr)
#     # Searching for the majority element
#     for key, value in count.items():
#         if value > (n // 3):
#             return key
#     return -1
#
#
# nums = [2, 2, 1, 1, 1, 2, 2]
# ans = majority_element(nums)
# print(ans)

# Time Complexity: O(N log N)  Space Complexity: O(N)

# Optimal Approach

def majority_element(arr):
    n = len(arr)

    cnt1, cnt2 = 0, 0
    el1, el2 = float('-inf'), float('-inf')

    for i in range(n):
        if cnt1 == 0 and el2 != arr[i]:
            cnt1 = 1
            el1 = arr[i]
        elif cnt2 == 0 and el1 != arr[i]:
            cnt2 = 1
            el2 = arr[i]

        elif arr[i] == el1:
            cnt1 += 1
        elif arr[i] == el2:
            cnt2 += 1
        else:
            cnt1 -= 1
            cnt2 -= 1

    ls = []

    cnt1, cnt2 = 0, 0
    for i in range(n):
        if arr[i] == el1:
            cnt1 += 1
        if arr[i] == el2:
            cnt2 += 1

    mini = int(n / 3) + 1

    if cnt1 >= mini:
        ls.append(el1)
    if cnt2 >= mini:
        ls.append(el2)

    return ls


arr = [11, 33, 33, 11, 33, 11]
ans = majority_element(arr)
print(ans)

# Time Complexity: O(N)  Space Complexity: O(1)
