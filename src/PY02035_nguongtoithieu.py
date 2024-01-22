s = input()
k = int(input())
a = {}
i = 0
tmp = ''
while i<len(s):
    tmp += s[i]
    i+=1
    if i%2==0:
        if tmp not in a:
            a[tmp] = 1
        else:
            a[tmp] += 1
        tmp = ''
d = 0
l = sorted(a.keys())
for i in l:
    if a[i]>=k:
        print(f'{i} {a[i]}')
        d = 1
if d==0: print("NOT FOUND")
        