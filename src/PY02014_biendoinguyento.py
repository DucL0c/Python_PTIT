prime = [1]*10001
b = []
for i in range(2,10001):
    if prime[i]==1:
        for j in range(i*i,10001,i):
            prime[j] = 0
        b.append(i)
            
                    
n = int(input())
a = list(map(int,input().split()))
ans = 0
for i in a:
    s = 10**9
    for j in b:
        s = min(s,abs(j-i))
    ans = max(ans,s)
print(ans)