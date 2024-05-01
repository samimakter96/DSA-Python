candies = [2, 8, 7]
extraCandies = 3

ans = []
max_candie = float('-inf')
for i in range(len(candies)):
    if candies[i] > max_candie:
        max_candie = candies[i]

for i in range(len(candies)):
    if candies[i] + extraCandies >= max_candie:
        ans.append("true")
    else:
        ans.append("false")
print(ans)
