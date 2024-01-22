def ltron(f:float):
    n = int(f)
    tmp = f-n
    if tmp<0.25:
        return float(n)
    elif tmp>=0.25 and tmp<0.75:
        return n+0.5
    else:
        return float(n+1)

for _ in range(int(input())):
    a = list(map(float,input().split()))
    s = a[2]+a[3]
    if a[0]==3 or a[0]==4: 
        s += 2.5
    elif a[0]==5 or a[0]==6:
        s += 3.0
    elif a[0]>=7 and a[0]<=9:
        s += 3.5
    elif a[0]>=10 and a[0]<=12:
        s += 4.0
    elif a[0]>=13 and a[0]<=15:
        s += 4.5
    elif a[0]>=16 and a[0]<=19:
        s +=5.0
    elif a[0]>=20 and a[0]<=22:
        s += 5.5
    elif a[0]>=23 and a[0]<=26:
        s += 6.0
    elif a[0]>27 and a[0]<=29:
        s += 6.5
    elif a[0]>=30 and a[0]<=32:
        s += 7.0
    elif a[0]>=33 and a[0]<=34:
        s += 7.5
    elif a[0]>=35 and a[0]<=36:
        s += 8.0
    elif a[0]>=37 and a[0]<=38:
        s += 8.5
    elif a[0]>=39 and a[0]<=40:
        s += 9.0
    
    if a[1]==3 or a[1]==4: 
        s += 2.5
    elif a[1]==5 or a[1]==6:
        s += 3.0
    elif a[1]>=7 and a[1]<=9:
        s += 3.5
    elif a[1]>=10 and a[1]<=12:
        s += 4.0
    elif a[1]>=13 and a[1]<=15:
        s += 4.5
    elif a[1]>=16 and a[1]<=19:
        s +=5.0
    elif a[1]>=20 and a[1]<=22:
        s += 5.5
    elif a[1]>=23 and a[1]<=26:
        s += 6.0
    elif a[1]>27 and a[1]<=29:
        s += 6.5
    elif a[1]>=30 and a[1]<=32:
        s += 7.0
    elif a[1]>=33 and a[1]<=34:
        s += 7.5
    elif a[1]>=35 and a[1]<=36:
        s += 8.0
    elif a[1]>=37 and a[1]<=38:
        s += 8.5
    elif a[1]>=39 and a[1]<=40:
        s += 9.0
    
    print(ltron(s/4))