"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water
it can trap after raining.

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case,
6 units of rain water (blue section) are being trapped.
"""

# Brute Force Approach:
arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
n = len(arr)
res = 0
# traverse for every element of the array
for i in range(1, n-1):
    # find the maximum element on its left
    left = arr[i]
    for j in range(i):
        left = max(left, arr[j])

    # find the maximum element on its right
    right = arr[i]
    for j in range(i+1, n):
        right = max(right, arr[j])

    # update the maximum water
    res = res + (min(left, right) - arr[i])
print(res)

# Time Complexity: O(N^2)   Space Complexity: O(1)


# Better Approach:

height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
n = len(height)

left_max = [0] * n
right_max = [0] * n
water = 0

# Fill left array
left_max[0] = height[0]
for i in range(1, n):
    left_max[i] = max(left_max[i-1], height[i])

# Fill right array
right_max[n-1] = height[n-1]
for i in range(n-2, -1, -1):
    right_max[i] = max(right_max[i+1], height[i])


for i in range(0, n):
    water += min(left_max[i], right_max[i]) - height[i]
print(water)

# Time Complexity: O(N)     Space Complexity: O(N)


# Optimal Solution:


def trap_water(height):
    # Check if the height array is empty
    if height == 0:
        return 0

    # Initialize variables
    water = 0
    l = 0
    r = len(height) - 1
    left_max = height[l]
    right_max = height[r]

    # Use two pointers approach
    while l < r:
        # If the left side is smaller, move the left pointer
        if left_max < right_max:
            l = l + 1
            left_max = max(left_max, height[l])
            water += left_max - height[l]
        # If the right side is smaller, move the right pointer
        else:
            r = r - 1
            right_max = max(right_max, height[r])
            water += right_max - height[r]

    # Return the total trapped water
    return water


# Example usage
arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trap_water(arr))

# Time Complexity: O(N)     Space Complexity: O(1)

