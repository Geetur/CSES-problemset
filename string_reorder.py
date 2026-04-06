
from math import sin

print(__builtins__.__dict__)


s = input()
counts = [0 for i in range(26)]
for i in s:
    counts[ord(i) - ord("A")] += 1
skip_list = [i for i in range(len(counts)) if counts[i] != 0]
l,r = 0, 1
ans = ""
n = len(skip_list)
while r < n:
    l_val = counts[skip_list[l]]
    r_val = counts[skip_list[r]]
    if l_val:
        ans += chr(skip_list[l] + ord("A"))
        counts[skip_list[l]] -= 1
    else:
        l,r = r, r + 1
    if r_val:
        ans += chr(skip_list[r] + ord("A"))
        counts[skip_list[r]] -= 1
    else:
        r += 1
last_left = counts[skip_list[l]]
if l < n:
    if last_left == 0:
        print(ans)
    elif last_left >= 2:
        print(-1)
    else:
        ans += chr(skip_list[l] + ord("A"))
        print(ans)
else:
    print(ans)



