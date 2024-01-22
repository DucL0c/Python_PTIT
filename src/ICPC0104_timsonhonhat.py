for _ in range(int(input())):
    s = input()
    s += "*"
    res = 0
    ans = 10**19
    for i in range(0,len(s)):
        if s[i].isdigit():
            res = res*10 + int(s[i])
            if s[i+1].isalpha():
                ans = min(ans,res)
                res = 0
    print(ans)