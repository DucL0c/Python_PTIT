import math
def checkNT(n):
    if n<2: return 0
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return 0
    return 1

n = int(input())
a = list(map(int,input().split()))
c = [0]*1000
b = []
for i in a:
    if c[i]==0:
        b.append(i)
        c[i] = 1
sum1 = sum(b)
sum2 = 0
d = 0
for i in range(len(b)):
    sum2 += b[i]
    if checkNT(sum2)==1 and checkNT(sum1-sum2)==1:
        print(i)
        d = 1
        break
    
if d==0: print("NOT FOUND")