"""Example 1:
Input: arr = [0,1,2,3,4,5,6,7,8]
Output: [0,1,2,4,8,3,5,6,7]
Explanation: [0] is the only integer with 0 bits.
[1,2,4,8] all have 1 bit.
[3,5,6] have 2 bits.
[7] has 3 bits.
The sorted array by bits is [0,1,2,4,8,3,5,6,7]
"""

# Approach-1:
# a = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# b = []
# for i in a:
#     count = 0
#     for num in range(0, 31):
#         bit = (a[i] >> num) & 1
#         if bit == 1:
#             count = count+1
#     b.append(count)
# # Bubble sort implementation
# for i in range(len(a)-1):
#     for j in range(len(a)-1-i):
#         if b[j] > b[j+1] or (b[j] == b[j+1] and (a[j] > a[j+1])):
#             temp = b[j]
#             b[j] = b[j+1]
#             b[j+1] = temp
#
#             temp = a[j]
#             a[j] = a[j+1]
#             a[j+1] = temp
# print(a)


# Approach-2:

# count sets bits
a = [7, 8, 4, 9, 4]
b = []

for i in range(len(a)):
    count = 0
    for j in range(len(a)):
        bit = (a[i] >> j) & 1
        count += bit
    b.append(count)
for i in range(len(a)):
    print(f"{a[i]} ---> {b[i]}")
# print(b)
print("----------")
# Bubble sort implementation:
for i in range(len(a)-1):
    for j in range(len(a)-1):
        if b[j] > b[j+1] or (b[j] == b[j+1] and (a[j] > a[j+1])):
            temp = b[j]
            b[j] = b[j+1]
            b[j+1] = temp

            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp

for i in range(len(a)):
    print(f"{a[i]} ---> {b[i]}")


# Approach : 3
# count set bits

# def count_set_bits(num):
#     count = 0
#     while num > 0:
#         num = num & (num-1)
#         count += 1
#     return count
#
#
# b = []
# arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# for i in arr:
#     b.append(count_set_bits(i))
# # print(b)
#
# # Bubble sort implementation
# for i in range(len(arr)-1):
#     for j in range(len(arr)-1-i):
#         if b[j] > b[j+1] or (b[j] == b[j+1] and (arr[j] > arr[j+1])):
#             temp = b[j]
#             b[j] = b[j+1]
#             b[j+1] = temp
#
#             temp = arr[j]
#             arr[j] = arr[j+1]
#             arr[j+1] = temp
#
# print(arr)
