n = int(input())
a = list(map(int,input().split()))
i = 1
while i<len(a):
    if (a[i]+a[i-1])%2==0:
        del a[i]
        del a[i-1]
        if i!=1: i-=1
    else: i+=1
print(len(a))