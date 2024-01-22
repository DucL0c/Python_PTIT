import math
t = int(input())
def check(n):
    if n<2: return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0: return False
    return True
def solve(s):
    if check(len(s))==False: return False
    demnt=0
    demkont=0
    for i in s:
        if check(int(i))==True: demnt +=1
        else: demkont +=1
    if demnt<=demkont: return False
    return True

for _ in range(t):
    s = input()
    if solve(s): print("YES")
    else: print("NO")