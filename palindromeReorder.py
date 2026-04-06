from collections import deque
dic,odds, res = {}, set(), deque()
s = input()

for i in s:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
    if dic[i] % 2 != 0: 
        odds.add(i)
    else:
        odds.remove(i)
if len(odds) == 1 or not odds:
    if odds:
        res.append(odds.pop())
    for key, val in dic.items():
        res.extendleft([key] * (val // 2)); res.extend([key] * (val // 2))
    print("".join(res))
else:
    print("NO SOLUTION")
