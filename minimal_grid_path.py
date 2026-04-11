from functools import cache

n = int(input())

string_grid = [[i for i in input()] for _ in range(n)]

dp = [["" for i in range(n)] for j in range(n)]

for i in range(n):
    for j in range(n):
        if i == 0 and j == 0:
            continue
        elif i == 0:
            dp[i][j] = dp[i][j - 1] + string_grid[i][j]
        elif j == 0:
            dp[i][j] = dp[i - 1][j] + string_grid[i][j]
        else:
            dp[i][j] = min(dp[i - 1][j], dp[i][j-1]) + string_grid[i][j]
print(dp[-1][-1])


@cache
def dfs(i, j):

    if i >= n or j >= n:
        return "~"
    if i == n - 1 and j == n - 1:
        return string_grid[i][j]
    
    a = string_grid[i][j] + dfs(i + 1, j)
    b = string_grid[i][j] + dfs(i, j + 1)

    return min(a, b)

print(dfs(0, 0))

