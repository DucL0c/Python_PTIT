delim = ".?!"
a = []
while True:
    try:
        s = input().lower().strip()
        a += s.split()
    except Exception:
        break
res = ''
for i in a:
    if i[-1] in delim:
        res += i[0:len(i)-1]
        x = res[0].upper()
        res = x + res[1:len(res)]
        print(res)
        res = ''
    else:
        res += i + " "