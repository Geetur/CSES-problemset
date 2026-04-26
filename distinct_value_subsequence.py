
from collections import defaultdict

n= int(input())

arr = list(map(int, input().split()))

    
c = defaultdict(int)

for i in arr:
    c[i] += 1
ans = 1
for i in c.values():
    ans = ((i + 1)* ans) % (10**9+7)
print(ans-1)