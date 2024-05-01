# iterative

sum_ = 0
n = 5
for i in range(0, 10, 2):
    if i == n:
        break
    sum_ += i

print(sum_)


def calculate_sum(i, n):
    if i >= 10 or i == n:
        return 0
    else:
        return i + calculate_sum(i + 2, n)


# You can replace 5 with any number manually
n = 5
result_sum = calculate_sum(0, n)
print(result_sum)
