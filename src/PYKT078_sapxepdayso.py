for _ in range(int(input())):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.insert(a.index(max(a)),k)
    b = [x for x in a if x<0]
    c = [x for x in a if x>=0]
    for i in b : print(i, end = " ")
    for i in c : print(i, end = " ")
    print()