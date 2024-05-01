"""
You have develop a application that basically reduce the length of string .

the logic behind that is you can remove zero or more than zero consecutive characters from string and replace with the
no of characters removed .

You are testing your application you have two strings str1 and str2 . check whether str2 is valid reduced string of str1
if yes return True else return False.

Example 1:
Input:
str1 = "SHARPENER"
str2 = "S3P3R"

Output: True
Explanation: We can clearly see that T is a valid compressed string for S. anbody
"""


def is_valid_reduced_string(str1, str2):

    i = 0
    j = 0

    while i < len(str1) and j < len(str2):
        if str1[i] == str2[j]:
            i += 1
            j += 1
        elif str2[j].isdigit():
            count = 0
            while j < len(str2) and str2[j].isdigit():
                count = count * 10 + int(str2[j])
                j += 1
            i += count
        else:
            return False

    return i == len(str1) and j == len(str2)


str1 = "SHARPENER"
str2 = "S3P3R"
print(is_valid_reduced_string(str1, str2))


"""
sort the array based on the count of character 'a' in each string, and if the counts are equal, you want to prioritize
the string with a greater length
"""

arr = ["vaibhav", "almanac", "is", "fat", "button", "aabaca"]

# Custom Bubble Sort
for i in range(len(arr) - 1):
    for j in range(len(arr) - 1 - i):
        count_a_j = arr[j].count('a')
        count_a_j1 = arr[j + 1].count('a')

        if count_a_j < count_a_j1 or (count_a_j == count_a_j1 and len(arr[j]) < len(arr[j + 1])):
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print(arr)

"""
Pro Strings You have given two strings . You have to perform a single swap operation to make these strings same if 
it can be then they are pro strings.
If pro strings are formed then return True else return False.
Note : if initially two equal strings are there then they are not pro strings .

Example 1:
Input: S1 = "sharpener", S2 = "pharsener"
Output: True
Explanation: We can swap the 0th and 4th character of S2 to make it equal to S1

Example 2:
Input: S1 = "sharpener", S2 = "sharpener"
Output: False
Explanation: Equal strings are not considered as pro strings.

Example 3:
Input: S1 = "badboy", S2 = "bbdaoy"
Output: True
Explanation: We can swap the 1st and 3rd character of S2 to make it equal to S1.

Example 4:
Input: S1 = "badboy", S2 = "abdaoy"
Output: False
Explanation: No Swapping will help us get the String S1."""