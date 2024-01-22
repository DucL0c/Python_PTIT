n = int(input())
a = []
for _ in range(n):
    s = input()+" "
    tong = 0
    for i in range(len(s)):
        if s[i].isdigit():
            tong = tong*10+int(s[i])
        else:
            if s[i-1].isdigit():
                a.append(tong)
                tong = 0
a.sort()
for i in a:
    print(i)