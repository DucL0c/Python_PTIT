def round_h(n:float):
    tmp = int(n)
    s = n - tmp
    if s>=0.5:
        return tmp+1
    else:
        return tmp
    
for _ in range(int(input())):
    s = input()
    l = 10**(len(s)-1)
    n = int(s)
    i = 10
    while i<=l:
        n = round_h(n/i)*i
        i *= 10
    print(n)