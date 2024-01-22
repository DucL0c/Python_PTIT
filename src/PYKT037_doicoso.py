t = int(input())
for _ in range(0,t):
    n,b = map(int,input().split())
    ans = ""
    if(b==2):
        while(n!=0):
            ans += str(n%2)
            n//=2
        print(ans[::-1])
    else:
        du = 0
        while(n!=0):
            du = n%b
            if(du<10):
                ans += str(du)
            else: 
                ans += chr(55+du)
            n //= b
        print(ans[::-1])