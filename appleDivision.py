from functools import cache


n = int(input())
arr = list(map(int, input().split()))

s = sum(arr)
half = s // 2
def dfs(i, curr):
    if i >= len(arr) or curr >= half:
        return abs(curr - (s - curr))
    a = dfs(i + 1, curr + arr[i])
    b = dfs(i + 1, curr)

    return min(a,b)

print(dfs(0, 0))




