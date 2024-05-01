"""
Given an integer n, return the number of prime numbers that are strictly less than n.

Example 1:
Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

Example 2:
Input: n = 0
Output: 0
"""

n = 10
# initial edge Cases (0, 1 non-prime by definition)
if n <= 2:
    print(0)
# all numbers initialized as prime, and then discounted via 'Sieve of Eratosthenes' algorithm
# naturally, our list is of size(n)
primes = [True] * n
primes[0] = primes[1] = False   # 0, 1 is always false because it's not a prime number

# for all elements in the range (2 , n)
for number in range(2, n):
    # if it is prime: True
    if primes[number]:
        # print(number, end=" ")    # if i wanted to print the prime number

        # starting from 2 * prime and ending at n - in increments of prime
        for multiple in range(number * number, n, number):
            primes[multiple] = False    # make all multiple prime is false
# Sum of Total Booleans
print(sum(primes))

"""
Time Complexity: O(n log log n) for the Sieve of Eratosthenes.
Space Complexity: O(n)
"""
