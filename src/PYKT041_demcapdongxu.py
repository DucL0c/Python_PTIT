import math
def C(n,k):
    if k<0 and k>n:
        return 0
    return math.comb(n,k)

n = int(input())
a = []
for i in range(n):
    a.append(input())

ans = 0
for i in range(n):
    dc = 0
    dh = 0
    for j in range(n):
        if a[i][j]=='C':
            dh += 1
        if a[j][i]=='C':
            dc += 1
    ans += C(dh,2) + C(dc,2)
print(ans)   