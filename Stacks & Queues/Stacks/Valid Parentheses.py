"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

Example 1:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
"""


def is_valid(s):
    # Initialize an empty stack to keep track of opening brackets
    stack = []

    # Define a dictionary to store pairs of opening and closing brackets
    pairs = {'(': ')', '{': '}', '[': ']'}

    # Iterate through each bracket in the input string
    for bracket in s:
        # If the bracket is an opening bracket, push it onto the stack
        if bracket in pairs:
            stack.append(bracket)
        else:
            # If the bracket is a closing bracket:
            # - Check if the stack is empty (no corresponding opening bracket)
            # - Check if the top of the stack matches the expected opening bracket
            if len(stack) == 0 or bracket != pairs[stack.pop()]:    # if the popped opening bracket is '(', pairs['('] would give ')'.
                # If one condition is true, return False (invalid string)
                return False

    # After iterating through all brackets, check if the stack is empty
    # If it's empty, all opening brackets have a corresponding closing bracket
    # If not, there are unmatched opening brackets
    if len(stack) == 0:
        return True
    else:
        return False


# Example usage:
s = "()[]{}"
print(is_valid(s))  # Output: True



# second approach
def is_valid(s):
    stack = []
    opening_brackets = '({['
    closing_brackets = ')}]'

    for bracket in s:
        if bracket in opening_brackets:
            # If it's an opening bracket, push onto the stack
            stack.append(bracket)
        elif bracket in closing_brackets:
            # If it's a closing bracket, check if the stack is not empty
            if not stack:
                return False

            # Check if the closing bracket matches the top of the stack
            top = stack.pop()
            if opening_brackets.index(top) != closing_brackets.index(bracket):
                return False

    # After iterating through all brackets, the stack should be empty for a valid string
    return not stack


# Example usage:
s = "()[]{}"
print(is_valid(s))  # Output: True
