t = int(input())
def solve(s):
    sum=0
    t = 1
    dem = 0
    deml = 0
    for i in range(0,len(s),2):
        if s[i]=='0': dem+=1
        else: t *= int(s[i])
        deml += 1
    for i in range(1,len(s),2):
        sum += int(s[i])
    if dem == deml: print(0)
    else: print(t,end = " ")
    print(sum)

for _ in range(t):
    s = input()
    solve(s)