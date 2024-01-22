t = int(input())
f = [0]*26
for i in range(1,26):
    if i == 1: f[i] = 1
    else: f[i] = f[i-1]*2 + 1
for i in range(t):
    n,k = map(int,input().split())
    while k<=f[n]:
        if k==f[n]//2+1:
            print(chr(64+n))
            break
        elif k>f[n]//2+1:
            k -= (f[n]//2 + 1)
            n -= 1
        elif k<f[n]//2+1:
            n-=1
    