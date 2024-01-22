import math
def check(n):
    if n<2: return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

n,m = map(int,input().split())
a = []
for _ in range(n):
    a.append(list(map(int,input().split())))
Max = 0
for i in range(n):
    for j in range(m):
        if check(a[i][j]):
            Max = max(Max,a[i][j])
if Max == 0: 
    print("NOT FOUND")
else:
    print(Max)
    for i in range(n):
        for j in range(m):
            if a[i][j]==Max:
                print(f"Vi tri [{i}][{j}]")