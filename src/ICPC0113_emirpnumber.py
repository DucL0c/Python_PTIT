import math
a = 0
def prime(n):
    if n<2: return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
def solve(s):
    if s == s[::-1]: return False
    if int(s[::-1])>a: return False
    if prime(int(s)) == False: return False
    if prime(int(s[::-1]))==False: return False
    return True

for _ in range(int(input())):
    a = int(input())
    check = {}
    for i in range(1,a):
        check[i] = 1
    for i in range(1,a):
        if check[i]==1:
            x = str(i)
            if solve(x) and solve(x[::-1]):
                print(x,end = " ")
                print(x[::-1],end = " ")
                check[i] = 0
                check[int(x[::-1])] = 0
    print()