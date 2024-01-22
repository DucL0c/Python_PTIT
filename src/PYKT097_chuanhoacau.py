delim = '?.!'
l = []
while True:
    try:
        s = input().strip().lower()
        if s[-1] not in delim:
            s += '.'
        l += s.split()
        if l[-1] in delim:
            x = l.pop()
            y = l.pop()
            l.append(y+x)
    except Exception:
        break
res = ""
for i in l:
    if i[-1] in delim:
        res += i
        x = res[0].upper()
        res = x + res[1:len(res)]
        print(res)
        res =''
    else:
        res += i + ' '