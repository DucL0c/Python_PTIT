def converT(s:str):
    tong = 0
    x = s[::-1]
    for i in range(len(x)):
        if i==0 and x[i]=='1':
            tong += 1
        elif i==1 and x[i]=='1':
            tong += 2
        elif i==2 and x[i]=='1':
            tong += 4
        elif i==3 and x[i]=='1':
            tong += 8
    return str(tong)
        
for _ in range(int(input())):
    b = input()
    x = input()
    ans = ""
    if b=='2':
        print(x)
    elif b=='4':
        n = len(x)
        while n>=2:
            tmp = x[n-2:n]
            n-=2
            ans += converT(tmp)
        if n!=0: ans += converT(x[0:n])
        print(ans[::-1])
    elif b=='8':
        n = len(x)
        while n>=3:
            tmp = x[n-3:n]
            n-=3
            ans += converT(tmp)
        if n!=0: ans += converT(x[0:n])
        print(ans[::-1])
    elif b=='16':
        n = len(x)
        while n>=4:
            tmp = x[n-4:n]
            n-=4
            a = converT(tmp)
            if a == '10': ans += 'A'
            elif a == '11': ans += 'B'
            elif a == '12': ans += 'C'
            elif a == '13': ans += 'D'
            elif a == '14': ans += 'E'
            elif a == '15': ans += 'F'
            else: ans += a
        if n!=0: ans += converT(x[0:n])
        print(ans[::-1])
