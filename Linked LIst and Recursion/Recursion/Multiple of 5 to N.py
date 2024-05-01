def print_output(n):
    if n < 0:
        return
    else:
        print_output(n - 5)
        print(5 * (n // 5))  # Ensure that you get multiples of 5


n = 25
print_output(n)
