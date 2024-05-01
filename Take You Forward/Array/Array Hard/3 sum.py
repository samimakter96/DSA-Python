# Brute Force Approach:
# arr = [-1, 0, 1, 2, -1, -4]
#
# st = set()
# n = len(arr)
# for i in range(n):
#     for j in range(i+1, n):
#         for k in range(j+1, n):
#             if arr[i] + arr[j] + arr[k] == 0:
#                 temp = [arr[i], arr[j], arr[k]]
#                 temp.sort()
#                 st.add(tuple(temp))
# # store the set item in the answer
# ans = [list(item) for item in st]
# print(ans)

# Time Complexity: O(N^3)  Space Complexity: O(N)


# Better Approach:

#
# def triplet(n, arr):
#
#     st = set()
#     for i in range(n):
#         hashset = set()
#         for j in range(i+1, n):
#             # calculate the third element
#             third = -(arr[i] + arr[j])
#
#             # if third element in the hashset
#             if third in hashset:
#                 temp = [arr[i], arr[j], third]
#                 temp.sort()
#                 st.add(tuple(temp))
#             hashset.add(arr[j])
#
#     # store the set in the answer
#     ans = list(st)
#     return ans
#
#
# arr = [-1, 0, 1, 2, -1, -4]
# n = len(arr)
# ans = triplet(n, arr)
# for it in ans:
#     print("[", end="")
#     for i in it:
#         print(i, end=" ")
#     print("]", end=" ")
# print()

# Time Complexity: O(N^2)  Space Complexity: O(N)

# Optimal Approach: Using two pointer


def triplet(n, nums):
    nums.sort()
    n = len(nums)
    ans = []

    # remove duplicate
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # moving two pointer
        j = i + 1
        k = n - 1
        while j < k:
            total_sum = nums[i] + nums[j] + nums[k]
            if total_sum < 0:
                j += 1
                while j < k and nums[j] == nums[j - 1]:
                    j += 1

            elif total_sum > 0:
                k -= 1
                while j < k and nums[k] == nums[k + 1]:
                    k -= 1
            else:
                ans.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1
                while j < k and nums[j] == nums[j - 1]:
                    j += 1
                while j < k and nums[k] == nums[k + 1]:
                    k -= 1

    return ans


arr = [-1, 0, 1, 2, -1, -4]
n = len(arr)
ans = triplet(n, arr)
for it in ans:
    print("[", end="")
    for i in it:
        print(i, end=" ")
    print("]", end=" ")
print()

# Time Complexity: O(N^2)  Space Complexity: O(1)
