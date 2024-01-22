n = int(input())
a = []
for i in range(0,n):
    x = list(map(int,input().split()))
    a.append(x)
k = int(input())
sum_t = 0
sum_d = 0
for i in range(0,n):
    for j in range(i+1,n):
        sum_t += a[i][j]
    for j in range(0,i):
        sum_d += a[i][j]
ans = abs(sum_t-sum_d)
if ans<=k: print("YES")
else: print("NO")
print(ans)