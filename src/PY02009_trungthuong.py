for _ in range(int(input())):
    n = int(input())
    myMap ={}
    for i in range(n):
        x = int(input())
        if x not in myMap:
            myMap[x] = 1
        else:
            myMap[x] += 1
    Max = max(myMap.values())
    ans = int(1e7)
    for i,j in myMap.items():
        if j == Max:
            ans = min(ans,i)
    print(ans)