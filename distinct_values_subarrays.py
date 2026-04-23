from collections import defaultdict
n = int(input())

arr = list(map(int, input().split()))

l, r = 0, 0
ans = 0
dic = defaultdict(int)
while r < n:
    dic[arr[r]] += 1
    while dic[arr[r]] >= 2:
        dic[arr[l]] -= 1
        if not dic[arr[l]]:
            del dic[arr[l]]
        l += 1
    ans += r - l + 1
    r += 1
print(ans)