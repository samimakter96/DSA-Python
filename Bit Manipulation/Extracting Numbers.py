"""Given a String Extract all numbers from it and store it inside an array. Return the Array Once extraction
is completed."""

s = "abc334v44d"
numbers = []  # Initialize an empty list to store the extracted numbers.
num = ""      # Initialize an empty string to store the current number.

for char in s:  # Loop through each character in the input string.
    if char.isdigit():  # Check if the current character is a digit.
        num += char  # If it's a digit, add it to the num string.
    elif num:  # If the character is not a digit and num is not empty, meaning we've collected a number.
        numbers.append(int(num))  # Append the collected number to the numbers list.
        num = ""  # Reset the num string to empty.

# Check if there's a number left in num at the end of the string.
if num:
    numbers.append(int(num))

print(numbers)


# Approach:2 solving via Ascii concept


def extract_numbers_from_string(s):
    numbers = []
    current_number = ""

    for char in s:
        # Check if the character's ASCII value is in the digit range.
        if 48 <= ord(char) <= 57:   # ASCII character encoding, the values for the digits '0' to '9' are from 48 to 57
            current_number += char
        else:
            # If the current_number is not empty, convert it to an integer and add to the list.
            if current_number:
                numbers.append(int(current_number))
            current_number = ""  # Reset current_number when a separator is encountered.

    # Add the last number if the string ends with a number.
    if current_number:
        numbers.append(int(current_number))

    return numbers


# Example usage:
str1 = "abc334v44d"
str2 = "abv345fjjf123tyir45jf6th"

output1 = extract_numbers_from_string(str1)
output2 = extract_numbers_from_string(str2)

print(output1)  # Output: [334, 44]
print(output2)  # Output: [345, 123, 45, 6]
