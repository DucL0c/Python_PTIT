import math
def prime(n):
    if n<2: return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
def solve(n):
    if prime(int(n))==False: return False
    if prime(int(n[::-1]))==False: return False
    sum = 0
    for i in n:
        sum += int(i)
    if prime(sum)==False: return False
    for i in n:
        if prime(int(i))==False: 
            return False
    return True

for _ in range(int(input())):
    n = input()
    if solve(n)==True: print("Yes")
    else: print("No")