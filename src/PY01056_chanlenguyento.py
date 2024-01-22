import math
t = int(input())
def check1(n):
    if n<2: return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0: 
            return False
    return True
def solve(s):
    sum = 0
    for i in s:
        sum += int(i)
    if check1(sum)==False: return False
    for i in range(0,len(s),2):
        if(int(s[i])%2!=0):
            return False
    for i in range(1,len(s),2):
        if(int(s[i])%2==0):
            return False
    return True

for _ in range(t):
    s = input()
    if(solve(s)): print("YES")
    else: print("NO")