"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""


def longest_common_prefix(strs):
    # First, we need to check if the array strs is empty. If it is, return an empty string
    if not strs:
        return ""
    # Initialize prefix with the first string: "flower"
    prefix = strs[0]
    # Loop through the remaining strings, start from 1 : "flow"
    for string in strs[1:]:
        i = 0
        # i is less than the length of the existing prefix. and i is less than the length of the current string (string)
        # and The characters at the current position (i) in both prefix and string are equal. then increment i by 1
        while i < len(prefix) and i < len(string) and prefix[i] == string[i]:
            i += 1
        # updates the prefix by slicing it up to the index i
        prefix = prefix[:i]

    return prefix


strs = ["flower", "flow", "flight"]
print(longest_common_prefix(strs))
# Time Complexity: o(m*n)   Space Complexity: o(n)


# Approach: 2
strs = ["flower", "flow", "flight"]
# initialize pre index 0: "flower"
pre = strs[0]
for i in strs:
    # if i not start with pre
    while not i.startswith(pre):
        # remove the last letter of pre
        pre = pre[:-1]
print(pre)
