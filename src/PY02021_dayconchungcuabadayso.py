for _ in range(int(input())):
    n,m,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = list(map(int,input().split()))
    i = j = x = d = 0
    while i<n and j<m and x<k:
        if a[i]==b[j] and b[j]==c[x]:
            print(a[i],end=" ")
            i+=1
            j+=1
            x+=1
            d = 1
        elif a[i]<b[j]: i+=1
        elif b[j]<c[x]: j+=1
        else: x+=1
    if d==0:
        print("NO")
    else: print()