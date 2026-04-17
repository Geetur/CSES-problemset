from collections import deque
import heapq
n = int(input())
queue = []
pairs = [(x, y) for x, y in (map(int, input().split()) for _ in range(n))]
pairs.sort(key = lambda x: x[0])
heapq.heapify(queue)
ans = 0
for x, y in pairs:
    while queue and x > queue [0][0]:
        heapq.heappop(queue)
    heapq.heappush(queue, (y, x))
    ans = max(ans, len(queue))
print(ans)