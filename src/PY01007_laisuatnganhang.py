t = int(input())
for _ in range(t):
    n,x,m = map(float,input().split())
    s = 0
    ans = 0
    while n<=m:
        s = n*x/100
        n += s
        ans += 1
    print(ans)