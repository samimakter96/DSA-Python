# def min_chars_to_make_palindrome(s):
#     count = 0  # Initialize a counter for added characters
#
#     # Check if the string is not a palindrome
#     while s != s[::-1]:
#         s = s[:-1]  # Remove the last character
#         count += 1  # Increment the counter for each character removed
#
#     return count  # Return the count of added characters
#
#
# # Example usage:
# input_string = "abracadabra"
# result = min_chars_to_make_palindrome(input_string)
# print(f"Minimum characters to add: {result}")


def min_chars_to_make_palindrome(s):
    start = 0
    end = len(s) - 1
    count = 0

    # Check if the string is already a palindrome
    while start < end:
        if s[start] != s[end]:
            # Add character from the end to the start
            s = s[:start] + s[end] + s[start:]
            count += 1
        # Move pointers towards the center
        start += 1
        end -= 1

    # Check if the modified string is a palindrome
    if s == s[::-1]:
        return count
    else:
        return count + 1  # Add one more character if needed to make it a palindrome


# Test cases
print(min_chars_to_make_palindrome("abcd"))  # Output: 3
print(min_chars_to_make_palindrome("aa"))  # Output: 0
