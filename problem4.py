n = int(input())
arr = list(map(int, input().split()))

ans = 0

for i in range(1, n):
    if arr[i] < arr[i - 1]:
        change = (arr[i - 1] - arr[i]); ans += change; arr[i] += change


print(ans)