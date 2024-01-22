import math
def checkNT(n):
    if n<2: return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
def tong(n):
    sum = 0
    while n>0:
        sum += n%10
        n //= 10
    return sum
for _ in range(int(input())):
    a,b = map(int,input().split())
    gcd = math.gcd(a,b)
    if checkNT(tong(gcd))==True:
        print("YES")
    else:
        print("NO")