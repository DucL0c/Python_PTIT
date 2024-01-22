for _ in range(int(input())):
    s = input()
    n = input()
    c = len(n)
    dem = 0
    i = 0
    while i<len(s)-2:
        x = s[i:i+c]
        if x == n:
            dem+=1
            i+=c
        else: i+=1
    print(dem)       