for _ in range(int(input())):
    n,m = list(map(int,input().split()))
    a = list(map(int,input().split()))
    for i in range(m,n,1):
        print(a[i],end = " ")
    for i in range(0,m,1):
        print(a[i],end = " ")    
    print()    