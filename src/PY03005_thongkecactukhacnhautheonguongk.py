m = {}
n,k = map(int,input().split())
for i in range(n):
    s = ''
    for i in input().lower() + ' ' :
        if (i >= 'a' and i <= 'z') or (i >= '0' and i <= '9') : s += i
        else :
            if(s != '') :
                if s in m : m[s] += 1
                else : m[s] = 1
                s = ''
s_map = dict(sorted(m.items(), key=lambda a:(-a[1],a[0])))
for i,j in s_map.items():
    if j>=k:
        print(f'{i} {j}')