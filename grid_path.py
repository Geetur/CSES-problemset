n = int(input())

dp = [[0 for i in range(n)] for j in range(n)]
dp[0][0] = 1
lines = [input() for _ in range(n)]
for i,z in enumerate(lines):
    for j, k in enumerate(z):
        if k == "*":
            dp[i][j] = k
for i in range(n):
    for j in range(n):
        if dp[i][j] == "*":
            continue
        if i == 0 and j == 0:
            continue
        if j != 0 and i != 0 and dp[i][j - 1] != "*" and dp[i - 1][j] != "*":
            dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % (10 ** 9 + 7)
            
        elif j != 0 and dp[i][j - 1] != "*":
            dp[i][j] = dp[i][j - 1]
        elif i != 0 and dp[i - 1][j] != "*":
            dp[i][j] = dp[i - 1][j]

if dp[0][0] == "*":
    print(0)
elif dp[-1][-1] == "*":
    print(0)
else:
    print(dp[-1][-1] % (10 ** 9 + 7))
        