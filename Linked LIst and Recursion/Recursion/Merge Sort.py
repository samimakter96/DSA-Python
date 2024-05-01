from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge_sort(nums):

            if len(nums) > 1:
                mid = len(nums) // 2
                left_num = nums[:mid]   # left num 0 to mid (not include mid)
                right_num = nums[mid:]

                # Recursively sort the left and right sub-arrays
                merge_sort(left_num)
                merge_sort(right_num)

                i = 0
                j = 0
                k = 0

                # Merge the sorted sub-arrays
                while i < len(left_num) and j < len(right_num):
                    if left_num[i] < right_num[j]:
                        nums[k] = left_num[i]
                        i = i + 1
                    else:
                        nums[k] = right_num[j]
                        j = j + 1
                    k = k + 1

                # Check for any remaining elements in left_num
                while i < len(left_num):
                    nums[k] = left_num[i]
                    i = i + 1
                    k = k + 1

                # Check for any remaining elements in right_num
                while j < len(right_num):
                    nums[k] = right_num[j]
                    j = j + 1
                    k = k + 1
        merge_sort(nums)
        return nums


# Example usage:
nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
solution = Solution()
sorted_nums = solution.sortArray(nums)
print(sorted_nums)
