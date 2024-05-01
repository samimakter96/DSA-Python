"""
There are many needy people who need some money are standing in a row .
the person who stands at i th position needs i*i rs money . You have X rs, and you want to fulfil the needs of people .
when you donate the money to any people it is deducted from X .
You have to find how many peoples can fulfil their needs by your money .

Example 1:

Input:
N = 14
Output: 3

Explanation: The needs of people is 1, 4, 9, 16, .... and so on. WE can fulfil needs of first 3 person ,
after which our money becomes 0 and we cant fulfil anyone else. So answer is 3
"""

x = 14  # money
count = 0   # count people need

i = 1   # count start from 1
while i * i <= x and count < x:
    x = x - i * i   # when we donate money it deducted from x
    count = count + 1  # count how many people fulfil their need
    i = i + 1   # # increase needy people by 1
print(count)
