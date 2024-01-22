n,m = map(int,input().split())
a = list(map(int,input().split()))
myMap = {}
for i in a:
    if i not in myMap:
        myMap[i] = 1
    else:
        myMap[i] += 1

tmp = set(myMap.values())
if(len(tmp)==1):
    print("NONE")
else:
    max1 = max(myMap.values())
    max2 = 0
    for i in myMap.values():
        if i>max2 and i<max1:
            max2 = i
    for i in range(1,m+1):
        if myMap[i] == max2:
            print(i)
            break