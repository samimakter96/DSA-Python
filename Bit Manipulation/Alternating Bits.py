"""Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always
have different values.
Example 1:
Input: n = 5
Output: true
Explanation: The binary representation of 5 is: 101

Example 2:
Input: n = 7
Output: false
Explanation: The binary representation of 7 is: 111.
"""

# n = 5
# binary = bin(n)[2:]
# for i in range(len(binary)-1):
#     if binary[i] == binary[i+1]:
#         print(False)
#         break
# else:
#     print(True)


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # Step 1: Convert the integer to binary representation
        binary = bin(n)[2:]

        # Step 2: Check whether the binary representation has alternating bits
        for i in range(len(binary) - 1):
            if binary[i] == binary[i + 1]:
                return False
        # Step 3: Return True if the binary representation has alternating bits, False otherwise
        return True


def main():
    n = int(input("Enter your number:"))
    s = Solution()
    output = s.hasAlternatingBits(n)
    if (output):
        print("true")
    else:
        print("false")


main()


# Approach : 2
n = 10
flag = 1
while n > 0:
    prev = n & 1   # 10 binary: 1010 right-most 0 is the prev
    curr = (n >> 1) & 1   # 10 binary: 1010 second right-most 1 is the curr
    if prev == curr:
        flag = 0
        print(False)
    if flag == 1:
        print(True)
    n = n >> 1  # after 1 right shift now n become = 5
