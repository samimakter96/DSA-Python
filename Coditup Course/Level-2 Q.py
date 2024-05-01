# Level-2 Questions
# Q.1 write a program to find sum of digits of a given number
i = int(input("Enter number to find sum of digits of a given numbers:"))
sum = 0
while i > 0:
    sum = sum + i % 10
    i = i // 10
print("sum of digits =", sum)

# Q.2 write a program to find sum of square of digits of a given number.
i = int(input("Enter number to find sum of square of a given number:"))
sum = 0
while i > 0:
    sum = sum + (i % 10) * (i % 10)
    i = i // 10
print("sum of square digits =", sum)

# Q.3 Write a program to find sum of cube of digits of a given number.
i = int(input("Enter number to find sum of cube of digits:"))
sum = 0
while i > 0:
    sum = sum + (i % 10)*(i % 10)*(i % 10)
    i = i // 10
print("sum of cube of each digits =", sum)

# Q.4 Write a program to check whether a given number is armstrong or not
i = int(input("Enter number to check for Armstrong:"))
orig = i
sum = 0
while i > 0:
    sum = sum + (i % 10)*(i % 10)*(i % 10)
    i = i // 10
if orig == sum:
    print("Number is Armstrong")
else:
    print("Number is not Armstrong")

# Q.5 Write a program to find product of digits of a given number.
i = int(input("Enter number:"))
prod = 1
while i > 0:
    prod = prod * (i % 10)
    i = i // 10
print("Product of digits =", prod)

# Q.6 write a program to find reverse of a give number
i = int(input("Enter number:"))
rev = 0
while i > 0:
    rev = (rev*10) + i % 10
    i = i // 10
print("Reverse =", rev)

# Q.7 write a program to check whether a given number is palindrome number or not
i = int(input("Enter number:"))
rev = 0
x = i
while i > 0:
    rev = (rev*10) + i % 10
    i = i // 10
if x == rev:
    print("Palindrome number")
else:
    print("Not palindrome number")

# Q.8 write a program to check whether a number is prime or not ?
n = int(input("Enter number:"))
count = 0
i = 1
while i <= n:
    if n % i == 0:
        count = count+1
    i = i + 1
if count == 2:
    print("prime number")
else:
    print("Not prime number")

# Q.9 write a program to print factorial of a given number
i = int(input("Enter number:"))
fac = 1
while i > 0:
    fac = fac*i
    i = i-1
print("Factorial =", fac)

# Q.20 write a program to print fibonacci series upto a given number
n = int(input("Enter number:"))
x = 0
y = 1
z = 0
while z <= n:
    print(z)
    x = y
    y = z
    z = x+y

# Q.21 write a program to print table of a given number
x = int(input("Enter number to find table:"))
for y in range(1, 11):
    print(x * y)
