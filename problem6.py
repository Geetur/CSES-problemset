
end = int(input())

for _ in range(end):
    y, x = map(int, input().split())
    
    n = max(y,x)
    base = ((n * n) - n) + 1

    if y == x:
        print(base)
    elif y > x:
        if n % 2 != 0:
            print(base - abs(y - x))
        else:
            print(base + abs(y - x))
    else:
        if n % 2 != 0:
            print(base + abs(y - x))
        else:
            print(base - abs(y - x))




