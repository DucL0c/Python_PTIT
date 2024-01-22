from datetime import datetime
tg = [0,25,34,50,80]
class KH:
    def __init__(self, ma, ten, phong, nd, ndi, pp):
        self.ma = self.setID(ma)
        self.ten = ten
        self.phong = phong
        self.songay = self.setSN(nd, ndi)
        self.tien = self.setT(phong, pp)

    def setID(self, i):
        return 'KH'+str(i).zfill(2)

    def setSN(self, nd, ndi):
        s1 = datetime.strptime(nd, "%d/%m/%Y")
        s2 = datetime.strptime(ndi, "%d/%m/%Y")
        s = (s2-s1).days
        return s+1

    def setT(self, phong, pp):
        return tg[int(phong[0])]*self.songay + pp

    def __str__(self):
        return f'{self.ma} {self.ten} {self.phong} {self.songay} {self.tien}'


n = int(input())
l = []
for i in range(n):
    ten = input().strip()
    phong = input().strip()
    nd = input().strip()
    ndi = input().strip()
    pp = int(input())
    l.append(KH(i+1, ten, phong, nd, ndi, pp))

l.sort(key=lambda a: (-a.tien))
for i in l:
    print(i)
