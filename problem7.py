
n = int(input())
if ((n * (n + 1) / 2) / 2) % 1 != 0:
    print("NO")
else:
    print("YES")

    target = (n * (n + 1) // 2) // 2

    s,c, res, res2 = 0,0,  "", ""

    avoid = 0

    for i in range(n, 0, -1):
        if not avoid:
            if target - s <= i:
                avoid = target - s; res += str(target - s)
                res2 += str(i) + " " if i != target - s else ""
                print(c + 1); print(res)
            else:
                s += i; c += 1; res += str(i) + " "
        elif i != avoid:
            if avoid == 1:
                res2 += str(i) + " " if i != 2 else str(i)
            else:
                res2 += str(i) + " " if i != 1 else str(i)
    print(n - (c + 1))
    print(res2)