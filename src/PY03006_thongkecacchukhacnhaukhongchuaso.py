m = {}
n = int(input())
for i in range(n):
    s = ''
    for i in input().lower() + ' ' :
        if (i >= 'a' and i <= 'z') : s += i
        else :
            if(s != '') :
                if s in m : m[s] += 1
                else : m[s] = 1
                s = ''
s_map = dict(sorted(m.items(), key=lambda a:(-a[1],a[0])))
for i,j in s_map.items():
    print(f'{i} {j}')