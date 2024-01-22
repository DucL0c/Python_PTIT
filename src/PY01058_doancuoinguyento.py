import math
t = int(input())
def check(n):
    if n<2: return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
for _ in range(t):
    s = input()
    l = len(s)
    res = s[l-4]+s[l-3]+s[l-2]+s[l-1]
    res = int(res)
    if check(res)==True: print("YES")
    else: print("NO")