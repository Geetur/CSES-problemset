
from functools import cache




num_books, budget = map(int, input().split())

books_prices = list(map(int, input().split()))

pages_per_book = list(map(int, input().split()))

dp = [[0 for i in range(budget + 1)] for j in range(num_books)]



for i in range(num_books):
    for j in range(budget + 1):
        skip = dp[i-1][j]
        take = 0
        if j - books_prices[i] >= 0:
            take = dp[i-1][j-books_prices[i]] + pages_per_book[i]
        dp[i][j] = max(skip, take)
print(dp[-1][-1])


@cache
def dfs(budget, i):
    if i >= num_books or budget < 0:
        return 0
    
    skip = 0 + dfs(budget, i + 1)
    take = 0
    if budget - books_prices[i] >= 0:
        take = pages_per_book[i] + dfs(budget - books_prices[i], i + 1)

    return max(skip, take)
