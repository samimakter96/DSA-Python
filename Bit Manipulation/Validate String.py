"""Given A String check whether on reversal it is the same or not.
Return True if yes otherwise return False.
Example 1:
Input:- word = "madam"
Output : true
Explanation:-
madam when reversed is the same as the original one.
"""


# s = input("Enter a string:")
# rev = s[-1::-1]
# if s == rev:
#     print("true")
# else:
#     print("false")


# this approach handle edge cases:
s = input("Enter any string:")
# Initialize an empty string to store the cleaned-up version
reversed_s = ""

# Iterate through each character in the input string 's'
for i in s:
    # Check if the character 'i' is a letter (a to z, both lowercase and uppercase)
    if i.isalpha():
        # If it's a letter, add it to the reversed_s string after converting it to lowercase
        reversed_s += i.lower()

# 'reversed_s' now contains the lowercase version of the input string 's'
if s == reversed_s[-1::-1]:
    print("true")
else:
    print("false")