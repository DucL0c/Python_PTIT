def rotate(s:str,sum1):
    tmp = ""
    for i in s:
        tmp += chr((ord(i)-ord('A') + sum1)%26 + ord('A')) 
    return tmp

n = int(input())
for _ in range(n):
    s = input()
    l = len(s)
    a = ""
    b = ""
    sum1 = 0
    sum2 = 0
    for i in range(0,int(l/2)):
        sum1 += ord(s[i])-ord('A')
        a += s[i]
    for i in range(int(l/2),l):
        sum2 += ord(s[i])-ord('A')
        b += s[i]
    a = rotate(a,sum1)
    b = rotate(b,sum2)
    ans = ""
    for i,j in zip(a,b):
        ans += chr( (ord(i)-ord('A') + ord(j)-ord('A'))%26 + ord('A') )
    print(ans)