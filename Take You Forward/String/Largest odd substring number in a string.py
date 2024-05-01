"""
You are given a string num, representing a large integer. Return the largest-valued odd integer (as a string) that is
a non-empty substring of num, or an empty string "" if no odd integer exists. A substring is a contiguous sequence of
characters within a string.

Example 1:
Input: num = "52"
Output: "5"
Explanation: The only non-empty substrings are "5", "2", and "52". "5" is the only odd number.

Example 2:
Input: num = "4206"
Output: ""
Explanation: There are no odd numbers in "4206".

Example 3:
Input: num = "35427"
Output: "35427"
Explanation: "35427" is already an odd number
"""

# This problem essentially requires you to find and return the largest odd integer substring from the given input string
# If there's no odd integer in any substring, the function should return an empty string.

# Brute Force Approach:
num = "52"
max_odd = ""
# fist we have to calculate the substring
for i in range(len(num)):
    for j in range(i, len(num)):
        substring = num[i:j+1]  # i:j+1 mens j inclusive
        # the substring is not empty and represents an odd integer
        if substring and int(substring) % 2 != 0:
            # This part checks if max_odd is an empty string, and then it compare with int(substring)
            if not max_odd or int(substring) > int(max_odd):
                max_odd = substring
print(max_odd)
# Time Complexity: O(N^2)   Space Complexity: O(1)


# Optimal Approach:
""" we can check if a give string is a even or odd from checking the last digit"""

# Given code
def max_odd(s):
    # The code iterates through the string in reverse order, starting from the last character (len(s) - 1) and moving
    # towards the beginning.
    for i in range(len(s) - 1, -1, -1):
        # It stops at the first occurrence of an odd digit in reverse order
        if int(s[i]) % 2 == 1:
            # The code extracts the substring from the beginning of the original string up to the index where the
            # first odd digit is encountered.
            return s[:i+1]   # s[:i+1] means "from the beginning up to index i (inclusive),
    return ""


# Driver code
s = "35427"
ans = max_odd(s)

# Function call
print(ans)

# Time Complexity: O(N)   Space Complexity: O(1)
