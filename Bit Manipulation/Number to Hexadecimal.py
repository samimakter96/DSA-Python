class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        hex_chars = "0123456789abcdef"  # List of hexadecimal characters
        result = []  # Initialize an empty list to store the hexadecimal digits

        # Convert negative numbers using two's complement
        if num < 0:
            num += 2 ** 32  # Convert negative number to its positive equivalent

        while num > 0:
            digit = num % 16  # Extract the remainder when divided by 16
            result.append(hex_chars[digit])  # Append the corresponding hex character to the result list
            num //= 16  # Divide the number by 16 for the next iteration

        return ''.join(result[::-1])    # Reverse the list and join the elements to form the hexadecimal representation