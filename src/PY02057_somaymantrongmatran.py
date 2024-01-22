n,m = map(int,input().split())
a = []
for _ in range(n):
    a.append(list(map(int,input().split())))
Max = 0
Min = int(1e7)
for i in range(n):
    for j in range(m):
        Max = max(Max,a[i][j])
        Min = min(Min,a[i][j])
ans = Max - Min
d = 0
for i in range(n):
    for j in range(m):
        if ans==a[i][j]:
            d = 1
if d == 0:
    print("NOT FOUND")
else:
    print(Max-Min)
    for i in range(n):
        for j in range(m):
            if Max-Min == a[i][j]:
                print(f"Vi tri [{i}][{j}]")