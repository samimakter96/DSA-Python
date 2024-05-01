"""
Example 1:
Input: s = "the sky is blue"
Output: "blue is sky the"

Example 2:
Input: s = "  hello world  "
Output: "world hello"
"""

s = "  hello world  "
s = s.split()
print(s)
rev = s[::-1]
print(rev)
print(" ".join(rev))


# reverse a string

st = "the sky is blue"
st = st.split()
new_str = ""
i = len(st) - 1
while i >= 0:
    new_str += st[i]

    # Add a space if it's not the last word
    if i > 0:
        new_str += " "

    i -= 1

print(new_str)
# Time Complexity: O(N)  Space Complexity: O(N)


# Optimal Solution:
st = "sky is the blue"
# st = "  hello world"  # edge cases
# st = "a good   example"  # edge cases

# Trim leading and trailing spaces
st = st.strip()
left = 0
right = len(st) - 1
temp = ""
ans = ""

while left <= right:
    ch = st[left]
    # if ch not = ' ' / empty means something in the ch then add ch to temp
    if ch != ' ':
        temp += ch
    # if ch is == empty ' '
    elif ch == ' ':
        # if ans not = empty string it means something is already in the string then add ans = temp + " " + ans
        if ans != "":
            ans = temp + " " + ans
        # if ans = empty string, means ans is empty string then add ans = temp
        else:
            ans = temp
        # resetting temp for the next word
        temp = ""
        # Skip over consecutive spaces
        while left <= right and st[left] == " ":
            left += 1
        continue
    # increment left + 1
    left += 1
# If not an empty string then add to the result (Last word is added)
if temp != "":
    if ans != "":
        ans = temp + " " + ans
    else:
        ans = temp

print(ans)
# Time Complexity: O(N)  Space Complexity: O(1)
