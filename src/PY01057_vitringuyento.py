import math
t = int(input())
def check(n):
    if n<2: return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
def solve(s):
    for i in range(0,len(s)):
        if check(i)==True and check(int(s[i]))==False:
            return False
        elif check(i)==False and check(int(s[i]))==True:
            return False
    return True
for _ in range(t):
    s = input()
    if solve(s)==True: print("YES")
    else: print("NO")