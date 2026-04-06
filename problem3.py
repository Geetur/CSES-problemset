
def solution(s):
    dic = {}
    l, r, ans = 0, 0, 0
    while len(s) > r:
        if s[r] in dic:
            dic[s[r]] += 1
        else:
            dic[s[r]] = 1
        while len(dic) > 1:
            dic[s[l]] -= 1
            if not dic[s[l]]:
                del dic[s[l]]
            l += 1
        ans = max(dic[s[r]], ans); r += 1
    print(ans)
solution(input())
        