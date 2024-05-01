"""
Given two sorted arrays, arr1, and arr2 of size n and m. Find the union of two sorted arrays.
The union of two arrays can be defined as the common and distinct elements in the two arrays.NOTE: Elements in
the union should be in ascending order.

Example 1:
Input:
n = 5,m = 5.
arr1[] = {1,2,3,4,5}
arr2[] = {2,3,4,4,5}
Output:
 {1,2,3,4,5}

Explanation:
Common Elements in arr1 and arr2  are:  2,3,4,5
Distnict Elements in arr1 are : 1
Distnict Elemennts in arr2 are : No distinct elements.
Union of arr1 and arr2 is {1,2,3,4,5}
"""

# Brute Force Approach: (Using Map/ Dictionary)

arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 3, 4, 4, 5]
union = []

freq_map = {}
for i in arr1:
    freq_map[i] = freq_map.get(i, 0) + 1

for i in arr2:
    freq_map[i] = freq_map.get(i, 0) + 1

for num in freq_map:
    union.append(num)
print(union)

# Time Complexity: O( (m+n)log(m+n) )   Space Complexity: O(m+n)

# Approach 2: Using Set
arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 3, 4, 4, 5]
union = []

s = set()

for num in arr1:
    s.add(num)

for num in arr2:
    s.add(num)

for num in s:
    union.append(num)
print(union)

# Optimal Solution:


def find_union(a, b):
    i, j = 0, 0  # Pointers
    union = []  # Union list

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:  # Case 1 and 2
            if len(union) == 0 or union[-1] != arr1[i]:
                union.append(arr1[i])
            i += 1
        else:  # Case 3
            if len(union) == 0 or union[-1] != arr2[j]:
                union.append(arr2[j])
            j += 1

    while i < len(arr1):  # If any elements left in arr1
        if union[-1] != arr1[i]:
            union.append(arr1[i])
        i += 1

    while j < len(arr2):  # If any elements left in arr2
        if union[-1] != arr2[j]:
            union.append(arr2[j])
        j += 1

    return union


arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr2 = [2, 3, 4, 4, 5, 11, 12]

print(find_union(arr1, arr2))

# Time complexity: O(m+n)