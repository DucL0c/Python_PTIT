import math
def checkNT(n):
    if n<2: return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
for _ in range(int(input())):
    n = int(input())
    dem = 0
    for i in range(1,n):
        if math.gcd(i,n)==1:
            dem+=1
    if checkNT(dem):
        print("YES")
    else:
        print("NO")