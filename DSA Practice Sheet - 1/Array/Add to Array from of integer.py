"""
Example 1:

Input: num = [1,2,0,0], k = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234
"""


def addToArrayForm(num, k):
    # Step 1: Convert array to integer
    num_as_int = 0
    for digit in num:
        num_as_int = (num_as_int * 10) + digit

    # Step 2: Add k to the integer
    sum_result = num_as_int + k

    # Step 3: Convert sum back to array
    result_array = []
    while sum_result > 0:
        result_array.append(sum_result % 10)
        sum_result //= 10

    # Step 4: Reverse the array
    result_array.reverse()

    return result_array


# Example
num = [1, 2, 0, 0]
k = 34
output = addToArrayForm(num, k)
print(output)
