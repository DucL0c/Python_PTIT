import sys
def sieve():
    N = 2000000
    prime = [0] * (N + 1)
    for i in range(2, N + 1):
        prime[i] = 0
    for i in range(2, int(N**0.5) + 1):
        if prime[i] == 0:
            for j in range(2 * i, N + 1, i):
                prime[j] = i
    for i in range(2, N + 1):
        if prime[i] == 0:
            prime[i] = i
    return prime

def tong(n, prime):
    if prime[n] == 0:
        return n
    s = 0
    while n != 1:
        s += prime[n]
        n //= prime[n]
    return s

prime = sieve()
sum = 0
for _ in range(int(sys.stdin.readline())):
    sum += tong(int(sys.stdin.readline()), prime)
print(sum)