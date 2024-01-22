t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort()
    b.sort()
    d = 1
    for i in range(n):
        if a[i]>b[i]:
            d = 0
            break
    if d==0: print("NO")
    else: print("YES")