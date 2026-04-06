from functools import cache

num_coins, target_sum = map(int, input().split())
coins = list(map(int, input().split())); coins.sort()


dp = [0] * (target_sum + 1)
dp[0] = 1
for coin in coins:
    for j in range(coin, len(dp)):
        dp[j] = (dp[j] + dp[j - coin]) % (10 ** 9 + 7)
print(dp[-1])

@cache
def dfs(i, target_sum):  
    if i >= len(coins) or target_sum < 0:
        return 0
    elif target_sum == 0:
        return 1
    
    skip, take = dfs(i + 1, target_sum), dfs(i, target_sum - coins[i])

    return skip + take

#print(dfs(0, target_sum))