"""Given two integers dividend and divisor, divide two integers without using multiplication,
 division, and mod operator.

 Example 1:
Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = 3.33333.. which is truncated to 3.
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = -2.33333.. which is truncated to -2.
 """


# Function to divide two integers without using multiplication, division, and mod operators
def divide(dividend, divisor):
    # Check for special cases
    if divisor == 0:
        raise ValueError("Cannot divide by zero")
    if dividend == 0:
        return 0

    # Determine the sign of the result
    sign = (dividend < 0) ^ (divisor < 0)  # True True/ False False = False, others True

    # Convert dividend and divisor to positive numbers
    dividend = abs(dividend)
    divisor = abs(divisor)

    quotient = 0  # Initialize the result

    # Subtract divisor from dividend until it can't be subtracted anymore
    while dividend >= divisor:
        dividend -= divisor
        quotient += 1

    # If the result should be negative, make it negative
    if sign:    # if sign True then -quotient execute
        quotient = -quotient

    # Ensure the result is within the 32-bit signed integer range
    if quotient < -2**31 or quotient > 2**31 - 1:
        return 2**31 - 1

    return quotient


# Example usage
dividend = 10
divisor = 3
result = divide(dividend, divisor)
print("Result:", result)  # Output should be 3


# Approach 2 for handle edge cases:
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        # Handle special cases
        if dividend == -2 ** 31 and divisor == -1:
            return 2 ** 31 - 1

        # Calculate the sign of the result
        sign = (dividend < 0) ^ (divisor < 0)

        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0

        # Bit manipulation to perform division
        while dividend >= divisor:
            temp, multiple = divisor, 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            dividend -= temp
            quotient += multiple

        return -quotient if sign else quotient

