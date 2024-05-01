# Strings are immutable

# strings operator
# 1. concatenation operator: (+)
# x = "Every" + "Day"
# print(x)

# 2. Replication operators: (*)
# a = 3 * "Hello"
# print(a)

# 3. Membership operator: (in/not in)
# syntax: <string> in <string>
#           <string> not in <string>

# i = "my name is samim"
# x = "i" in "samim"
# print(x)
# y = "i" not in "samim"
# print(y)

""" String Slicing """
# syntax: string[start:end:step_value]
# str_ = "hello world"
# print(str_[6:10])
# print(str_[6:])
# print(str_[:6])
# print(str_[3:-2])
# print(str_[:5])

# String function:
# len()
# a = "samim akter"
# print(len(a))

# program to find reverse of a string
# x = input("Enter string:")
# print(x[-1::-1])

# y = input("Enter a number:")
# for i in range(len(y)-1, -1, -1):
#     print(y[i], end=" ")

# Q. program to count total vowel and consonants in a string
# a = input("Enter a string:")
# vowel = 0
# cons = 0
# for i in range(0, len(a)):
#     if(a[i] !=" "):  # for space checking we don't count space
#         if (a[i] == "a" or a[i] == "e" or a[i] == "i" or a[i] == "o" or a[i] == "u"
#                 or a[i] == "A" or a[i] == "E" or a[i] == "I" or a[i] == "O" or a[i] == "U"):
#             vowel = vowel + 1
#         else:
#             cons = cons + 1
# print("Total Vowels =", vowel)
# print("Total Consonants =", cons)

"""String built-in function"""
# 1. len()
a = "samim akter"
print(len(a))

# 2. capitalize()
a = "samim"
b = a.capitalize()
print(a)
print(b)

# 3. find()
a = "rami is going to market"
b = "to"
print(a.find(b, 0, (len(a)-1)))

# 4. isalnum(): this function returns true if at least one character is alphabets or number
a = "ram123"
print(a.isalnum())
b = "hello"
print(b.isalnum())
c = "1234"
print(c.isalnum())

# 5. isdigit(): this function returns true if all the characters is digit
a = "1234"
print(a.isdigit())

# Q. program to check a string is palindrome or not
# a = input("Enter a string:")
# b = a[-1::-1]
# if a == b:
#     print("palindrome string")
# else:
#     print("Not palindrome")