"""
Remove duplicates from sorted array
"""

# Brute Force Approach:
arr = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5]

unique_list = []
seen = set()

for element in arr:
    if element not in seen:
        unique_list.append(element)
        seen.add(element)
print(unique_list)

"""
Time complexity: O(n*log(n))+O(n)
Space Complexity: O(n)
"""

# Optimal Approach (Best Solution):
# count the unique element: using Two pointers

arr = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5]
i = 0   # i points to the first unique element
for j in range(1, len(arr)):
    if arr[j] != arr[i]:
        i = i + 1   # Move the first pointer to the next unique element
        arr[i] = arr[j]   # Replace the next element after the unique one with the current different element
print("Number of unique element:", i + 1)  # we write i+1 because indexing starts from 0
print("Unique elements:", arr[:i + 1])  # 0 to i+1 means include i


# Time Complexity: O(N)
# Space Complexity: O(1)
