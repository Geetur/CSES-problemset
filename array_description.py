


n, m = map(int, input().split())
arr = list(map(int, input().split()))

MOD = 10**9 + 7


dp = [0] * (m + 2)

if arr[0] == 0:
    for v in range(1, m + 1):
        dp[v] = 1
else:
    dp[arr[0]] = 1
    
for i in range(1, n):
    new_dp = [0] * (m + 2)
    
    if arr[i] == 0:
        for v in range(1, m + 1):
            new_dp[v] = (dp[v - 1] + dp[v] + dp[v + 1]) % MOD
    else:
     
        v = arr[i]
        new_dp[v] = (dp[v - 1] + dp[v] + dp[v + 1]) % MOD
        
    
    dp = new_dp


ans = sum(dp[1:m+1]) % MOD
print(ans)


    
    



