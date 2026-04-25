n, target = map(int, input().split())
arr = list(map(int, input().split()))
arr = [(i, n) for i,n in enumerate(arr)]    
arr.sort(key = lambda x: x[1])
found = False
for i in range(len(arr) - 2):
    l, r = i + 1, len(arr) - 1
    while r > l:
        ii, ll, rr = arr[i][1], arr[l][1], arr[r][1]
        s = ii + ll + rr
        if s == target:
            print(arr[i][0]+1, arr[l][0]+1, arr[r][0]+1)
            found = True
            break
        elif s > target:
            r -= 1
        else:
            l += 1
    if found:
        break
if not found:
    print("IMPOSSIBLE")


