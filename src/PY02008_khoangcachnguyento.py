import math
prime = [0]*10001
def sieve():
    for i in range(10000):
        prime[i] = 1
    prime[0]=prime[1] = 0
    for i in range(2,int(math.sqrt(10000))+1):
        if prime[i]==1:
            for j in range(2*i,10000,i):
                prime[j]=0
sieve()
a,b = list(map(int,input().split()))
dem = 0
print(b,end = " ")
i = 2
while dem<a:
    if prime[i]==1:
        print(b+i,end = " ")
        b += i
        dem+=1
    i+=1