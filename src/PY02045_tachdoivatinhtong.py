n = input()
while len(n)>1:
    l = int(len(n)/2)
    a = n[l:]
    b = n[:l]
    n = str(int(a)+int(b))
    print(n)