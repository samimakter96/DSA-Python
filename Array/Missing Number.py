arr = [1, 3, 4, 5]
n = len(arr)
actual_sum = 0
for i in range(n):
    total_sum = (n+1)*(n+2)//2  # total sum including missing number
    actual_sum = actual_sum + arr[i]    # actual sum given in the array
    missing_number = total_sum - actual_sum

    print(missing_number)


# Approach:2
arr = [1, 3, 4]
n = len(arr)
current_sum = sum(arr)
expected_sum = (n+1) * (n+2) // 2   # sum of N natural number
missing_number = expected_sum - current_sum
print(missing_number)

