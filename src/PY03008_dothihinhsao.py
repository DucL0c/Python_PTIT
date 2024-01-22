n = int(input())
a = []
for _ in range(n+1):
    a.append([])
for _ in range(n-1):
    u,v = map(int,input().split())
    a[u].append(v)
    a[v].append(u)
d = 0
for i in range(1,n+1):
    if len(a[i])==1:
        d += 1
if d==n-1: print("Yes")
else: print("No")