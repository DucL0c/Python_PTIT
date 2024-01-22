for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    l = min(a)
    r = max(a)
    m = {}
    for i in a:
        if i not in m:
            m[i] = 1
        else:
            m[i] += 1
    ans = 0
    for i in range(l,r):
        if i not in m:
            ans+=1
    print(ans)