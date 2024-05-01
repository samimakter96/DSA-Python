def fibonacci(n):

    # Base Case
    if n == 0:
        return 0
    if n == 1:
        return 1

    else:
        return fibonacci(n-1) + fibonacci(n-2)


def main():
    n = int(input("Enter a number:"))
    output = fibonacci(n)
    print(output)


main()