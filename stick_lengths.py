n = int(input())

sticks = list(map(int, input().split()))

sticks.sort()
if n == 1:
    print(0)
else:
    mid = n // 2
    mid2 = mid - 1
    
    mid, mid2 = sticks[mid], sticks[mid2]
    min1, min2 = 0, 0
    
    for i in sticks:
        min1 += abs(i-mid)
        min2 += abs(i-mid2)
    
    print(min(min1, min2))
