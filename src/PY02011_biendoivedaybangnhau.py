n = int(input())
a = list(map(int,input().split()))
ans = 10**9
v = 0
for i in range(0,n):
    sum = 0
    for j in range(0,n):
        if j==i: continue
        else:
            sum += abs(a[j]-a[i])
    if sum<ans:
        ans = sum
        v = a[i]
print(f'{ans} {v}')