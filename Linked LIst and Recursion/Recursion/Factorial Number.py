def factorial_number(n):

    if n == 1:
        return 1

    else:
        return n * factorial_number(n - 1)


def main():
    n = 5
    output = factorial_number(n)
    print(output)


main()