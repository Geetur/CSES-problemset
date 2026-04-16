n = int(input())

arr = []

for _ in range(n):
    x, y = map(int,input().split())
    arr.append([x,y] )

arr.sort(key = lambda x: x[0])

ans = 1
for i in range(n-1):
    x, y = arr[i]
    if y <= arr[i + 1][0]:
        ans += 1
    else:
        arr[i + 1][1] = min(arr[i + 1][1], y)
print(ans)
