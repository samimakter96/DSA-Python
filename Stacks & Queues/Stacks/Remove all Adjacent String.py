"""
You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent
and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.
Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

Example 1:
Input: s = "abbaca"
Output: "ca"
Explanation:
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible
move. The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
Example 2:

Input: s = "azxxzy"
Output: "ay"

"""

# Approach: 1
s = "abbaca"
ans = []
for i in s:
    # if stack is non empty and last element of stack == current element i then we pop()
    if len(ans) > 0 and ans[-1] == i:
        ans.pop()
    else:
        ans.append(i)
print("".join(ans))

# Time Complexity: O(N)   Space Complexity: O(N)


# Approach : 2
s = "abbaca"
# Convert string to list to make it mutable
ans = list(s)
# Initialize pointer to keep track of the last valid position
pointer = 0

for i in range(len(s)):
    # If stack is non empty and last element of stack == current element i then we update pointer
    if pointer > 0 and ans[pointer - 1] == s[i]:
        pointer -= 1
    else:
        ans[pointer] = s[i]
        pointer += 1

# Convert the list back to string and consider only the valid characters
result = "".join(ans[:pointer])
print(result)

# Time Complexity: O(N)    Space Complexity: O(1)
