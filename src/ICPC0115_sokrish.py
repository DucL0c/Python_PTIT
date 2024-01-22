def giaithua(n):
    if n==0: return 1
    else: return n*giaithua(n-1)
for _ in range(int(input())):
    s = input()
    n = int(s)
    sum = 0
    for i in range(len(s)):
        sum += giaithua(int(s[i]))
    if sum==n: print("Yes")
    else: print("No")