n = int(input())
l = []
ans = {}
for i in range(n):
    s = input()
    if s=='':
        ans[l[0]] = len(l)-1
        l = []
    else:
        l.append(s)
for i,j in ans.items():
    print(f'{i}: {j}')
print(f'{l[0]}: {len(l)-1}')