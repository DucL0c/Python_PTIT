for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    myMap = {}
    for i in a:
        if i not in myMap:
            myMap[i] = 1
        else:
            myMap[i] += 1
    for i,j in myMap.items():
        if j%2!=0:
            print(i)