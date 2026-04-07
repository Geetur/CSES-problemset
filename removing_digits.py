

n = int(input())

dp = [0] * (n + 1)


for i in range(len(dp) - 1, -1, -1):
    if i != n and dp[i] <= 0:
        continue
    str_version = str(i)
    for j in str_version:
        int_digit = int(j)
        if dp[i - int_digit]:
            dp[i - int_digit] = min(dp[i - int_digit], dp[i] + 1)
        else:
            dp[i - int_digit] = dp[i] + 1

print(dp[0])