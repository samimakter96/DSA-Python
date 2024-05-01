# def generate_row(row):
#     ans = 1
#     ans_row = [1]   # inserting first element
#
#     # Calculate the rest of the element
#     for col in range(1, row):
#         ans *= (row - col)
#         ans //= col
#         ans_row.append(ans)
#     return ans_row
#
#
# def pascal_triangle(n):
#     ans = []
#
#     # Store the entire pascal triangle
#     for row in range(1, n+1):
#         ans.append(generate_row(row))
#     return ans
#
#
# n = 5
# print(pascal_triangle(n))


def generate(num_rows):

    result = []
    if num_rows == 0:
        return result

    first_row = [1]
    result.append(first_row)

    for i in range(1, num_rows):
        prev_row = result[i - 1]
        current_row = [1]

        for j in range(1, i):
            current_row.append(prev_row[j - 1] + prev_row[j])

        current_row.append(1)
        result.append(current_row)

    return result


num = 5
print(generate(num))
