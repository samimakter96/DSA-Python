class StockSpanner:
    def __init__(self):
        # Initialize an empty stack to store pairs of (price, span)
        self.stack = []

    def next(self, price: int) -> int:
        # Initialize span to 1 for the current stock
        span = 1

        # Calculate span for the current stock by checking the prices in the stack
        while self.stack and self.stack[-1][0] <= price:
            # Add the span of the stock at the top of the stack to the current span
            span += self.stack[-1][1]

            # Pop the stock from the stack since it won't be needed for future calculations
            self.stack.pop()

        # Append the current stock's price and span to the stack
        self.stack.append([price, span])

        # Return the span of the current stock
        return self.stack[-1][1]


# Instantiate StockSpanner object
obj = StockSpanner()

# Call the next method with stock prices
param_1 = obj.next(100)
param_2 = obj.next(80)
param_3 = obj.next(60)
param_4 = obj.next(70)
param_5 = obj.next(60)
param_6 = obj.next(75)
param_7 = obj.next(85)

# Print the results
print(param_1)  # Output: 1
print(param_2)  # Output: 1
print(param_3)  # Output: 1
print(param_4)  # Output: 2
print(param_5)
print(param_6)
print(param_7)
