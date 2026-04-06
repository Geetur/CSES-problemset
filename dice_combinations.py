
from collections import deque
n = int(input())
lower_range = 1
upper_range = 6 

dp = deque([1, 1, 2, 4, 8, 16])
if n <= 5:
    print(dp[n])
else:
    for i in range(n - 5):
        dp.append(sum(dp) % (10 ** 9 + 7))
        dp.popleft()
    print(dp[-1]) 





from functools import cache
@cache
#decrementing until zero, is same as incrementing until n
def dfs(n):
    if n == 0:
        return 1
    #irrelvant to tabulation since there is no negative index
    elif n < 0:
        return 0
    #turns into dp[i - 1] + dp[i - 2] . . . 
    return dfs(n - 1) + dfs(n - 2) + dfs(n - 3) + dfs(n - 4) + dfs(n - 5) + dfs(n - 6)

print(dfs(n))


    
