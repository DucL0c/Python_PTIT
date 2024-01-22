for _ in range(int(input())):
    s = input()
    a = s.split('.')
    d = 1
    if len(a)!=4: print("NO")
    else:
        for i in a:
            if i.isdigit():
                if int(i)<0 or int(i)>255:
                    d = 0
                    break
            else:
                d = 0
                break
        if d==0: print("NO")
        else: print("YES")