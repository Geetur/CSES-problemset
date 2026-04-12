import sys

num_children, max_weight = map(int, sys.stdin.readline().split())

children_weights = sorted(list(map(int, sys.stdin.readline().split())))

ans = 0

l, r = 0, len(children_weights) - 1

while l <= r:
    ans += 1
    if (children_weights[l] + children_weights[r]) > max_weight:
        r -= 1
    else:
        l += 1
        r -= 1
print(ans)
