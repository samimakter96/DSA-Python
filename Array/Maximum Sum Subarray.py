# Given an array find the maximum sum subarray.

arr = [5, 2, -4, -5, 3, -1, 2, 3, 1]
n = len(arr)
max_sum = arr[0]
for i in range(0, n):
    prev_sum = 0
    for j in range(i, n):
        prev_sum = prev_sum+arr[j]
        if prev_sum > max_sum:
            max_sum = prev_sum
print("Maximum sum subarray is =", max_sum)

# solution 2: using kadane,s algorithm
arr = [4, -3, -2, 2, 3, 1, -2, -3, 6, -4, 2, 1]
n = len(arr)
curr_sum = 0
max_sum = arr[0]
for i in range(0, n):
    curr_sum = curr_sum+arr[i]
    if curr_sum > max_sum:
        max_sum = curr_sum
    if curr_sum < 0:
        curr_sum = 0
print("Maximum sum subarray is =", max_sum)

# def maximum_sum_subarray(arr):
#     n = len(arr)
#     max_sum_subarray = arr[0]
#     current_sum = 0
#     st = 0; end = 0; pos = 0
#
#     for i in range(len(arr)):
#         current_sum = current_sum + arr[i]

#         if current_sum > max_sum_subarray:
#             max_sum_subarray = current_sum
#             st = pos
#             end = i
#         elif current_sum < 0:
#             current_sum = 0
#             pos = i + 1
#     print("Maximum sum subarray is=", max_sum_subarray )
#     print("start index of the window=", st)
#     print("end index of the window=", end)
#
#
# arr = [4,-3, -2, 2, 3, 1, -2, -3, 6, -6, -4, 2, 1]
# maximum_sum_subarray(arr)

arr = [-6, -5, -6, -2, -3]
max_sum = arr[0]
for i in range(len(arr)):
    for j in range(i, len(arr)):
        sum_sub = 0
        for k in range(i, j+1):
            # print(arr[k], end="")
            sum_sub = sum_sub + arr[k]
            if sum_sub > max_sum:
                max_sum = sum_sub
        # print()
        # print("sum of the sub array:", sum_sub)
print("maximum sum subarray:", max_sum)

arr = [-6, -5, -2, -3]
max_sum = arr[0]
for i in range(len(arr)):
    prev_sum = 0
    for j in range(i, len(arr)):
        prev_sum = prev_sum + arr[j]
        if prev_sum > max_sum:
            max_sum = prev_sum
print("maximum sum sub array:", max_sum)
















