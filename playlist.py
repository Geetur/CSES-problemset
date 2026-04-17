n = int(input())

arr = list(map(int, input().split()))

dic = {}
l,r = 0, 0
ans = 0
while r < len(arr):
    while arr[r] in dic:
        dic[arr[l]] -= 1
        if dic[arr[l]] == 0:
            del dic[arr[l]]
        l += 1
    dic[arr[r]] = 1
    ans = max(ans, len(dic))
    r += 1

print(ans)

