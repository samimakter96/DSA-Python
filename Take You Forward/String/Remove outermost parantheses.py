"""
Example 1:

Input: s = "(()())(())"
Output: "()()()"
Explanation:
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
"""


def removeOuterParentheses(s):
    result = ""
    count = 0

    # Iterate through each character in the input string
    for char in s:
        if char == '(':
            # If it's not the outermost opening parenthesis, add to the result
            if count > 0:
                result += char
            # Increase the count for an opening parenthesis
            count += 1
        else:
            # Decrease the count for a closing parenthesis
            count -= 1
            # If it's not the outermost closing parenthesis, add to the result
            if count > 0:
                result += char

    return result


# Example usage:
input_string = "(())(())(()())"
output_string = removeOuterParentheses(input_string)
print(output_string)


s = "(()())(())"
res = ""
count = 0
for char in s:
    if char == "(":
        if count > 0:
            res = res + char
        count = count + 1
    else:
        count = count - 1
        if count > 0:
            res = res + char
print(res)
