t = int(input())
def solve(s):
    for i in range(1,len(s)):
        if int(s[i])<int(s[i-1]):
            return False
    return True

for _ in range(t):
    s = input()
    if solve(s): print("YES")
    else: print("NO")