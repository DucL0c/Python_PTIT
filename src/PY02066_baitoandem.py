# for _ in range(int(input())):
n = int(input())
a = []
while len(a)<n:
    b = list(map(int,input().split()))
    a += b
d=0
for i in range(1,a[len(a)-1]+1):
    if i not in a:
        print(i)
        d = 1
if d==0: print("Excellent!")