import math
from collections import defaultdict
def check_nt(n):
    if n<2: return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
n = input()
dick = defaultdict(int)
a = list(map(int,input().split()))
for i in a:
    if check_nt(i):
        dick[i]+=1
for num,count in dick.items():
    print(f"{num} {count}")