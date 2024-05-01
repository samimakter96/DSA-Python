# Q.1 Write a program to print from 1 to 10.
i = 1
while i <= 10:
    print(i)
    i = i+1

# Q.2 Write a program to print from 1 to n.
n = int(input("Enter number up-to which you want to print:"))
i = 1
while i <= n:
    print(i)
    i = i+1

# Q.3 write a program to print from 10 to 1.
i = 10
while i >= 1:
    print(i)
    i = i-1

# Q.4 write a program to print from n to 1.
n = int(input("Enter number:"))
while n >= 1:
    print(n)
    n = n-1

# Q. write a program to print sum of n to 1
n = int(input("Enter number:"))
sum_ = 0
while n > 0:
    sum_ += n
    n = n - 1
print(sum_)

# Q.5 write a program to find sum from 1 to n.
n = int(input("Enter number up to which you want to sum:"))
i = 1
sum_ = 0
while i <= n:
    sum_ = sum_ + i
    i = i + 1
print("sum =", sum_)

# Q.6 write a program to print sum of SQUARE from 1 to n.
n = int(input("Enter number up-to which you want to sum:"))
i = 1
sum1 = 0
while i <= n:
    sum1 = sum1 + i*i
    i = i+1
print("sum =", sum1)

# Q.7 Write a program to find sum of even digits and product of odd digits of a given number:
n = int(input("Enter a number:"))
even_sum = 0
prod = 1
while n > 0:
    digit = n % 10
    if digit % 2 == 0:
        even_sum = even_sum + digit
    elif digit % 2 == 1:
        prod = prod * digit
    n = n // 10
print("sum of even digits =", even_sum)
while n > 0:
    digit = n % 10
    if digit % 2 == 1:
        prod = prod * digit
    n = n // 10
print("product of odd digits of a given number =", prod)

# Q.8 write a program to print sum of CUBE from 1 to n.

n = int(input("Enter number upto which you want to sum:"))
i = 1
sum = 0
while i <= n:
    sum = sum + i*i*i
    i = i+1
print("sum =", sum)

# Q.9 write a program to print only even numbers between 1 to n.
n = int(input("Enter number up-to which you want to print:"))
i = 2
while i <= n:
    print(i)
    i = i+2

# solution 2:
n = int(input("Enter number:"))
i = 1
while i <= n:
    if i % 2 == 0:
        print(i)
    i = i+1

# Write a program to print only ODD numbers between 1 to n.

n = int(input("Enter number:"))
i = 1
while i <= n:
    if i % 2 != 0:
        print(i)
    i = i+1

# Q.10 Write a program to find sum of even numbers from 1 to n.

n = int(input("Enter number:"))
i = 1
sum = 0
while i <= n:
    if i % 2 == 0:
        sum = sum+i
    i = i + 1
print("sum of even numbers =", sum)

# Write a program to find sum of Odd numbers from 1 to n.
n = int(input("Enter number:"))
i = 1
sum = 0
while i <= n:
    if i % 2 == 1:
        sum = sum+i
    i = i + 1
print("sum of odd numbers =", sum)

# Q.11 Write a program to find sum of first n even numbers.
n = int(input("How many even number you want to add:"))
i = 1
sum = 0
count = 0
while count < n:
    if i % 2 == 0:
        sum = sum+i
        count = count+1
    i = i+1
print("Sum of Even numbers =", sum)