# How to find length of a subarray
# arr = [10, 20, 30, 40, 50, 60, 70]
# start = 2
# end = 5
# subarray_length = end - start+1
# print("Length of the subarray", subarray_length)

# Define the array
my_array = [10, 20, 30, 40, 30, 50, 60, 70]

# Specify the element to search for
target_element = 30

# Initialize variables to store start and end indices
start = None
end = None

# Iterate through the array
for i in range(len(my_array)):
    if my_array[i] == target_element:
        if start is None:
            # Found the first occurrence, set it as the start index
            start = i
        # Update the end index with each occurrence
        end = i

# Check if the element was found in the array
if start is not None:
    subarray_length = end - start + 1
    print("Starting index:", start)
    print("Ending index:", end)
    print("Length of the subarray:", subarray_length)
else:
    print("Element not found in the array.")

arr = [1, 4, 2, 5, 3]
n = len(arr)
sum_odd = 0
for i in range(n):
    for j in range(i+1, n+1):
        if (j-i) % 2 != 0:
            sum_odd = sum_odd+sum(arr[i:j])
print(sum_odd)


# Approach : 2
# Define the array
a = [1, 4, 2, 5, 3]

# Initialize a variable to store the total sum
total_sum = 0

# Loop through the array
for i in range(len(a)):
    # For each element, we consider sub-arrays with odd lengths
    for j in range(i, len(a), 2):
        # Extract the subarray from index i to j
        subarray = a[i:j + 1]

        # Check if the subarray length is odd
        if len(subarray) % 2 == 1:
            # Calculate and add the sum of the subarray to the total_sum
            total_sum += sum(subarray)

# Print the total sum of odd length sub arrays
print("Sum of odd length subarray:", total_sum)


arr = [1, 4, 2, 5, 3]
odd_sum_subarray = 0
for row in range(len(arr)):
    for column in range(row, len(arr), 2):
        subarray = arr[row: column+1]
        odd_sum_subarray += sum(subarray)
print(odd_sum_subarray)
