# Reverse a Array: Using two pointer

arr = [1, 2, 3, 4, 5, 6]
left = 0
right = len(arr)-1

while left <= right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1
print(arr)

# Time Complexity: O(N)    Space Complexity: O(1)


# Reverse a String: Using two pointer
s = "America"

# Convert the string to a list
s_list = list(s)

# Initialize pointers
start = 0
end = len(s_list) - 1

# Swap characters using two pointers
while start < end:
    # Swap characters at start and end indices
    temp = s_list[start]
    s_list[start] = s_list[end]
    s_list[end] = temp

    # Move pointers towards each other
    start += 1
    end -= 1

# Join the list back into a string
result = ''.join(s_list)

print(result)
