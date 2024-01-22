import math
def check(n):
    if n<2: return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

n = int(input())
a = list(map(int,input().split()))
l = []
for i in a:
    if check(i):
        l.append(i)
l.sort()
for i in a:
    if check(i):
        print(l.pop(0),end=" ")
    else: print(i,end=" ")