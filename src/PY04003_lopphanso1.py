import math
class phanso:
    def __init__(self,tu,mau):
        self.tu = tu
        self.mau = mau
    def toigian(self):
        gcd = math.gcd(self.tu,self.mau)
        self.tu //= gcd
        self.mau //=gcd
        print('{}/{}'.format(self.tu,self.mau))

tu,mau = map(int,input().split())
a = phanso(tu,mau)
a.toigian()