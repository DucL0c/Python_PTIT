def sieve_eratosthenes(N):
    is_prime = [True] * (N + 1)
    is_prime[0] = is_prime[1] = False
    primes = []

    for p in range(2, N + 1):
        if is_prime[p]:
            primes.append(p)
            for i in range(2 * p, N + 1, p):
                is_prime[i] = False

    return primes

def count_numbers(L, R, primes):
    count = 0
    for num in range(L, R + 1):
        is_divisible = False
        for prime in primes:
            if prime * prime > num:
                break
            if num % prime == 0:
                is_divisible = True
                break
        if not is_divisible:
            count += 1
    return count

while True:
    L, R = map(int, input().split())
    if L == -1:
        break
    N = int(input())
    primes = sieve_eratosthenes(N)
    result = count_numbers(L, R, primes)
    print(result)
