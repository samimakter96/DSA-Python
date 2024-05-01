# write a program to store first n prime number in an array
# n = 5
# arr = []
# count = 0
# x = 2
# while count < n:
#     flag = True
#     for i in range(2, x):
#         if x % i == 0:
#             flag = False
#             break
#     if flag == True:
#         arr.append(x)
#         count = count+1
#     x = x+1
# print(arr)


n = 5
arr = []
count = 0
x = 2
while count < n:
    flag = True
    for i in range(2, int(x ** 0.5)+1):
        if x % i == 0:
            flag = False
            break
    if flag:
        arr.append(x)
        count = count+1
    x = x+1
print(arr)


n = int(input("Enter number how many prime number you want:"))

prime_number = []
count = 0
num = 2
while count < n:
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        prime_number.append(num)
        count = count + 1
    num = num + 1
print(prime_number)


# Approach 2: Using Sieve of Eratosthenes method
n = int(input("Enter how many prime numbers you want to print:"))
prime = [True] * (n * 10)  # Increase the size to avoid out-of-range errors
prime[0] = prime[1] = False
prime_numbers = []
count = 0
num = 2

while count < n:
    if prime[num]:
        prime_numbers.append(num)
        count += 1
        for multiple in range(num * num, n * 10, num):
            prime[multiple] = False
    num += 1

print("Prime numbers:", prime_numbers)
