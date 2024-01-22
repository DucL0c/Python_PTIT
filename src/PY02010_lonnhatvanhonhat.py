while True:
    n = int(input())
    if n==0: break
    l = []
    for i in range(0,n):
        l.append(int(input()))
    d = 1
    for i in range(0,n-1):
        if l[i]!=l[i+1]:
            d = 0
    if d==1:
        print("BANG NHAU")
    else:
        print(f"{min(l)} {max(l)}")
