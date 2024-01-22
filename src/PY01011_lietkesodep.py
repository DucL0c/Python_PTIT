a = []
b = ['0', '2', '4', '6', '8']
def Try(s) :
    ans = s + s[::-1]
    a.append(ans)
    if(len(s) != 3) :
        for i in b :
            Try(s + i)
            
for i in range(1, 5) : Try(b[i])
a.sort()
t = int(input())
for i in range(t) :
    n = int(input())
    for j in a :
        if int(j) < n : print(j, end = " ")
        else : break
    print()