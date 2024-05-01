# Write a function that takes an unsigned integer and returns the number of '1' bits it has
# (also known as the Hamming weight).


def hammingWeight(n):
    # Initialize a variable to keep track of the count of '1' bits
    count = 0

    # Loop through the bits of the unsigned integer until it becomes 0
    while n:
        # Increment the count if the least significant bit is 1
        count += n & 1

        # Right-shift the integer by 1 bit to check the next bit
        n >>= 1

    # Return the final count of '1' bits
    return count


print(hammingWeight(10))


# using for loops

n = 30
count = 0
for i in range(n):
    count = count + (n & 1)
    n >>= 1
print(count)
