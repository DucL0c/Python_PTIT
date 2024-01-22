for _ in range(int(input())):
    s = input()
    s += "*"
    res = 0
    ans = -1
    for i in range(0,len(s)):
        if s[i].isdigit():
            res = res*10 + int(s[i])
            if s[i+1].isalpha():
                ans = max(ans,res)
                res = 0
    print(max(ans,res))