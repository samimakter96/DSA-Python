# Rotate Array by one

# Left Shift:
# arr = [1, 2, 3, 4, 5, 6, 7]
# temp = arr[0]
# for i in range(len(arr)-1):
#     arr[i] = arr[i+1]
# arr[len(arr)-1] = temp
# print("Left shift the array by one:", arr)


# Right Shift:
# arr = [1, 2, 3, 4, 5, 6, 7]
# temp = arr[len(arr)-1]
# for i in range(len(arr)-1, -1, -1):
#     arr[i] = arr[i-1]
# arr[0] = temp
# print("Right shift the array by one:", arr)


"""
Rotate the array by k position
"""
# Brute Force Approach:
# Left Shift:
# arr = [1, 2, 3, 4, 5, 6, 7]
# k = 3
# k = k % len(arr)
#
# for count in range(k):
#     temp = arr[0]
#     for i in range(len(arr)-1):
#         arr[i] = arr[i+1]
#     arr[len(arr)-1] = temp
# print("array after k left rotation:", arr)

# Right Shift:
arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
k = k % len(arr)
for count in range(k):
    temp = arr[len(arr)-1]
    for i in range(len(arr)-1, -1, -1):
        arr[i] = arr[i-1]
    arr[0] = temp
print("array after k right rotation:", arr)

# TC: O(N^2)  SC: O(1)


# Better Approach:
# left shift
arr = [1, 2, 3, 4, 5, 6, 7]
n = len(arr)
k = 2
k = k % n   # Calculate k modulo n: k % n = 2 % 7 = 2

temp = [0] * k  # Create a temporary array temp of size k: temp = [0, 0]
# Copy the first k elements from arr to temp: temp = [1, 2]
for i in range(k):  # 0 to 2
    temp[i] = arr[i]

# Shift the elements in arr to the left by k positions:
for i in range(k, n):   # 2 to 7
    arr[i-k] = arr[i]   # arr[i-k] --> arr[2-2] = 0   arr[i] --> arr[2]

# Copy the elements from temp back to the end of arr:
for i in range(k):
    arr[n - k + i] = temp[i]
print("array after k left rotation:", arr)

# Time complexity: O(n)  Space Complexity: O(k)


# Right Shift:
arr = [1, 2, 3, 4, 5, 6, 7]
n = len(arr)
k = 2
k = k % n
temp = [0] * k
# Copy the last k elements from arr to temp: temp = [6, 7]
for i in range(n - k, n):   # 5 to 7
    temp[n - k - i] = arr[i]  # n-k-i --> 5-5 = 0

# Shift the elements in arr to the right by k positions:
for i in range(n - k - 1, - 1, - 1):   # n-k-1 --> 4 to 0
    arr[i + k] = arr[i]     # [i+k] --> 4 + 2 = 6

# Copy the elements from temp back to the beginning of arr:
for i in range(k):
    arr[i] = temp[i]
print("array after k right shift rotation:", arr)
# Time complexity: O(n)  Space Complexity: O(k)


# Best Approach: 2

arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
k = k % len(arr)
b = []
for i in range(len(arr)):
    b.append(0)
# print(b)

for i in range(len(arr)):
    new_pos = (i + k) % len(arr)    # for left shift (i-k) % len(arr)  --> + to -
    b[new_pos] = arr[i]
print("arr after k right shift rotation:", b)

# Time Complexity: O(N)   Space Complexity: O(N)


# Optimal Solution (Best Solution):

# Left shift
arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
k = k % len(arr)

st = 0
end = len(arr)-1
while st <= end:
    arr[st], arr[end] = arr[end], arr[st]
    st += 1
    end -= 1

st = 0
end = k
while st <= end:
    arr[st], arr[end] = arr[end], arr[st]
    st += 1
    end -= 1

st = k+1
end = len(arr)-1
while st <= end:
    arr[st], arr[end] = arr[end], arr[st]
    st += 1
    end -= 1
print(arr)

# Right Shift:

arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
k = k % len(arr)

st = 0
end = len(arr)-1
while st <= end:
    arr[st], arr[end] = arr[end], arr[st]
    st += 1
    end -= 1

st = 0
end = k-1
while st <= end:
    arr[st], arr[end] = arr[end], arr[st]
    st += 1
    end -= 1

st = k
end = len(arr)-1
while st <= end:
    arr[st], arr[end] = arr[end], arr[st]
    st += 1
    end -= 1
print(arr)

# Time Complexity: O(N)   Space Complexity: O(1)