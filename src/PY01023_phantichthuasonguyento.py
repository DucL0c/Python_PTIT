for _ in range(int(input())):
    n = int(input())
    myMap = {}
    i = 2
    while i<=n and n>0:
        if n%i==0:
            while n%i==0:
                if i not in myMap:
                    myMap[i] = 1
                else:
                    myMap[i] += 1
                n//=i
        else: i+=1
    print(f"1 * ",end="")
    ans = ' * '.join([f"{i}^{j}" for i,j in myMap.items()])
    print(ans)