import math
for _ in range(int(input())):
    n = input()
    m = n[::-1]
    gcd = math.gcd(int(n),int(m))
    if gcd == 1:
        print("YES")
    else:
        print("NO")