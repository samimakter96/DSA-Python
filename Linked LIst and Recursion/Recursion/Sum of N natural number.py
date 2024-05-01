def natural_number(n):

    if n == 0:
        return 0
    return n + natural_number(n - 1)


def main():
    n = 5
    output = natural_number(n)
    print(output)


main()