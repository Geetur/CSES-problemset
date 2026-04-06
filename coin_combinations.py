
num_coins, desired_sum = map(int, input().split())
coins = list(map(int, input().split()))
coins.sort(); coins = [i for i in coins if i <= desired_sum]


dp = [0] * (desired_sum + 1)
# for every desired_sumth state, we see if nth coin brings us to zero
dp[0] = 1
ways = 1
for i in range(1, len(dp)):
    for coin in coins:
        if i - coin >= 0:
            dp[i] = (dp[i] + dp[i-coin]) % (10 ** 9 + 7)
print(dp[-1])




    
