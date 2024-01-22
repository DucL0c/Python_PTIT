for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    myMap = {}
    num = int(1e7)
    for i in a:
        if i not in myMap:
            myMap[i] = 1
        else:
            myMap[i] += 1
    l = max(myMap.values())
    for i,j in myMap.items():
        if j == l:
            num = min(num,i)
    if l>n//2:
        print(num)
    else:
        print("NO")