arr = [1, 2, 3, 4, 5]
running_sum = []
sum_ = 0
for i in range(len(arr)):
    sum_ = sum_ + arr[i]
    running_sum.append(sum_)
print(running_sum)

# solution 2:

# a = [1, 2, 3, 4, 5]
# n = len(a)
# for i in range(1, n):
#     a[i] = a[i] + a[i-1]
# print("Running sum =", a)

nums = [1, 2, 3, 4, 5]
for i in range(1, len(nums)):
    nums[i] = nums[i] + nums[i - 1]

print(nums)