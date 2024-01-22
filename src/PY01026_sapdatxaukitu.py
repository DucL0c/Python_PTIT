def count(s):
    myMap = {}
    for i in s:
        if i not in myMap:
            myMap[i] = 1
        else:
            myMap[i] += 1
    return myMap
for k in range(1,int(input())+1):
    s1 = input()
    s2 = input()
    dem1 = count(s1)
    dem2 = count(s2)
    print(f"Test {k}: ",end="")
    if dem1==dem2: 
        print("YES")
    else:
        print("NO")
    