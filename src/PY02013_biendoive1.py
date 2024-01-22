while True:
    n = int(input())
    if n==0: break
    dem = 1
    if n==1: print(1)
    else:
        while n!=1:
            if n%2==0:
                n //=2
            else:
                n = n*3+1
            dem+=1
        print(dem)
        