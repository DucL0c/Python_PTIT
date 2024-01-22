for _ in range(int(input())):
    a,b = list(map(int,input().split()))
    c = min(a,b)
    d = max(a,b)
    s = input().split()
    if len(s)>1:
        x = s[0]
        y = s[1]
    else:
        x = s[0]
        y = input()
    print(int(x.replace(str(d),str(c))) + int(y.replace(str(d),str(c))),end = " ")
    print(int(x.replace(str(c),str(d))) + int(y.replace(str(c),str(d))))