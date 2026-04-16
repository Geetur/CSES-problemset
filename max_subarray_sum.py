n = int(input())

arr = list(map(int, input().split()))

curr = 0
ans = 0
for i in arr:
    if i + curr < 0:
        curr = 0
        continue
    else:
        curr += i
        ans = max(ans, curr)
if ans <= 0:
    print(max(arr))
else:
    print(ans)
