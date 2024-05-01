"""
ou are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future
to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
"""

# Brute Force Approach:
prices = [7, 1, 5, 3, 6, 4]
max_pro = 0
for i in range(len(prices)):
    for j in range(i+1, len(prices)):
        max_ = prices[j] - prices[i]
        if max_ > max_pro:
            max_pro = max_
print(max_pro)

# Time Complexity: O(N^2)   Space Complexity: O(1)


# Optimum Solution:
prices = [7, 1, 5, 3, 6, 4]

max_profit = 0
minimum_price = float('inf')

for i in range(len(prices)):
    if prices[i] < minimum_price:
        minimum_price = prices[i]

    profit = prices[i] - minimum_price

    if profit > max_profit:
        max_profit = profit
print(max_profit)

# Time Complexity: O(N)   Space Complexity: O(1)

# Using two pointer:
prices = [7, 1, 5, 3, 6, 4]

left = 0    # buy
right = 1   # sell
maximum_profit = 0

while right < len(prices):
    if prices[left] < prices[right]:
        profit = prices[right] - prices[left]

        if profit > maximum_profit:
            maximum_profit = profit
    else:
        left = right
    right = right + 1
print(maximum_profit)
