n = int(input())
a = []
for i in range(n):
    l = list(map(int,input().split()))
    a.append(l)
k = int(input())
sum_t = 0
sum_d = 0
for i in range(n):
    for j in range(0,n-i-1):
        sum_t += a[i][j]
    for j in range(n-i,n):
        sum_d += a[i][j]
if abs(sum_t-sum_d)<=k:
    print(f"{'YES'}\n{abs(sum_t-sum_d)}")
else:
    print(f"{'NO'}\n{abs(sum_t-sum_d)}")