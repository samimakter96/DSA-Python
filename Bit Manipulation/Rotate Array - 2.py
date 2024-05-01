# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

"""Try to Solve in time Complexity 0(n) with extra Space."""

a = [1, 2, 3, 4, 5, 6, 7]
k = 3
k = k % len(a)
b = []
for i in range(0, len(a)):
    b.append(0)
# print(b)
for i in range(0, len(a)):
    new_pos = (i + k) % len(a)
    b[new_pos] = a[i]
print(b)
""" Time Complexity O(n)"""
""" Space Complexity O(n) """


"""Left shift Rotation"""
a = [1, 2, 3, 4, 5]
k = 3
b = []
for i in range(len(a)):
    b.append(0)
for i in range(len(a)):
    new_pos = (i - k) % len(a)  # Changed '+' to '-'
    b[new_pos] = a[i]

print(b)
