import math
class phanso:
    def __init__(self,tu,mau):
        self.tu = tu
        self.mau = mau
    def tong(self,b):
        gcd = math.gcd(self.mau,b.mau)
        lc_m = (self.mau*b.mau)//gcd
        TU = self.tu*(lc_m//self.mau)  + b.tu*(lc_m//b.mau)
        MAU = lc_m
        gcd = math.gcd(TU,MAU)
        TU //= gcd
        MAU //=gcd
        print('{}/{}'.format(TU,MAU))

l = list(map(int,input().split()))
a = phanso(l[0],l[1])
b = phanso(l[2],l[3])
a.tong(b)