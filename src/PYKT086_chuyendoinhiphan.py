with open('DATA.in','r') as sc:
    t = int(sc.readline().strip())
    for i in range(0,t):
        b = int(sc.readline().strip())
        n = sc.readline().strip()
        if(b==2):
            print(n)
        else:
            tmp = 0
            ans = ""
            for j in range(0,len(n)):
                tmp += int(n[j])*pow(2,len(n)-1-int(j))
            while(tmp!=0):
                du = tmp%b
                if(du<10):
                    ans += str(du)
                else:
                    ans += chr(55+du)
                tmp//=b
            print(ans[::-1])