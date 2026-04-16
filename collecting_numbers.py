import heapq

n = int(input())

arr = [(n, i) for i,n in enumerate(map(int, input().split()))]
heapq.heapify(arr)
runs = 1
prev = heapq.heappop(arr)
while arr:
    curr = heapq.heappop(arr)
    if curr[1] < prev[1]:
        runs += 1
    prev = curr

print(runs)



