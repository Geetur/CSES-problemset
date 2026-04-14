n = int(input())
arr = list(map(int, input().split()))
arr.sort()
curr = 0
for i in arr:
    if i <= curr + 1:
        curr += i
    else:
        break
print(curr + 1)


    

    
    


