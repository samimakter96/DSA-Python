from typing import List


# Step 1: Define the function and its parameters
def generateFibonacciNumbers(n: int) -> List[int]:
    # Step 2: Base case
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    # Step 3: Recursive case
    else:
        # Recursively call the function to generate previous Fibonacci numbers
        fib_numbers = generateFibonacciNumbers(n - 1)

        # Calculate the next Fibonacci number by adding the last two numbers
        next_number = fib_numbers[-1] + fib_numbers[-2]

        # Append the next number to the list and return it
        fib_numbers.append(next_number)
        return fib_numbers


# Step 4: Test the function
n = 7
result = generateFibonacciNumbers(n)
print(f"The first {n} Fibonacci numbers are: {result}")


# Print Fibonacci Number : iterative way

n = 7

if n == 0:
    print(0)
else:
    second_last = 0   # for (i-2)th term
    last = 1        # for (i-1)th term
    print(second_last, last, end=" ")

    for i in range(2, n+1):
        curr = last + second_last
        second_last = last
        last = curr
        print(curr, end=" ")

# Time Complexity: O(N)  Space Complexity: O(1)
