n, q = map(int, input().split())
arr = list(map(int, input().split()))

pre = [0] * (n + 1)
s = 0
for i in range(n):
    s += arr[i]
    pre[i + 1] = s

for _ in range(q):
    l, r = map(int, input().split())
    print(pre[r] - pre[l - 1])
