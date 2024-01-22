def tangdan(i,s):
    for j in range(0,i):
        if int(s[j]) >= int(s[j+1]):
            return False
    return True
def giamdan(i,s):
    for j in range(i,len(s)-1):
        if int(s[j]) <= int(s[j+1]):
            return False
    return True

for _ in range(int(input())):
    s = input()
    d = 0
    if len(s)<3: print("NO")
    else:
        for i in range(len(s)):
            if tangdan(i,s)==True and giamdan(i,s)==True:
                d = 1
        if d==1: print("YES")
        else: print("NO")
    
    