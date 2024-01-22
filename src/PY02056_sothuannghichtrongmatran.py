def check(n):
    s = str(n)
    if len(s)<2: return False
    if s!=s[::-1]:
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
            if Max == a[i][j]:
                print(f"Vi tri [{i}][{j}]")