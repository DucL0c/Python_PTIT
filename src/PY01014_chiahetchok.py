b = []
a, K, N = map(int, input().split())
# i = 6 - (10%6) = 2
i = K - (a % K)   

N -= a

while i <= N:
    b.append(i)
    i += K

if (len(b) == 0):
    print(-1)
else:
    for i in b:
        print(i, end = ' ')