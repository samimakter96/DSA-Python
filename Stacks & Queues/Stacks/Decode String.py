"""
Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
"""

# 1. Keep adding to stack un-till you get "]"
# 2. When "]" is found, dont add "]" to stack, instead pop all characters until "[" is found, pop "[" too
# 3. Then keep popping till we have digits, keep adding to k
# 4. Multiply digit * string popped , and add this new string to stack


s = "3[a]2[bc]"
stack = []
for i in range(len(s)):
    if s[i] != "]":
        stack.append(s[i])   # step-1
    else:
        sub_str = ""
        while stack[-1] != "[":  # step-2
            sub_str = stack.pop() + sub_str
        stack.pop()

        k = ""
        while len(stack) > 0 and stack[-1].isdigit():   # step-3
            k = stack.pop() + k

        stack.append(int(k) * sub_str)   # step-4

print("".join(stack))

