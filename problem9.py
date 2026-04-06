n = int(input())

for i in range(1, n + 1):
    total = ((i * i) * ((i * i) - 1)) // 2
    if i > 2:
        total -= 4 * (i - 1) * (i - 2)
    print(total)




