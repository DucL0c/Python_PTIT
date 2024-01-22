from datetime import datetime
class MonHoc:
    def __init__(self,maMon,tenMon):
        self.maMon = maMon
        self.tenMon = tenMon

class CaThi:
    def __init__(self,ma,tmp:str):
        tmp = tmp.split()
        self.ma = ma
        self.maMon = tmp[0]
        self.tenMon = None
        for i in a:
            if i.maMon == self.maMon:
                self.tenMon = i.tenMon
                break
        self.nt = datetime.strptime(tmp[1],"%d/%m/%Y")
        self.gt = tmp[2]
        self.grt = tmp[3]

    def __str__(self):
        self.nt = (self.nt).strftime("%d/%m/%Y")
        return f"{self.ma} {self.maMon} {self.tenMon} {self.nt} {self.gt} {self.grt}"

n,m = map(int,input().split())
a = []
for _ in range(n):
    a.append(MonHoc(input(),input()))

b = []
for x in range(m):
    ma = 'T' + str(x+1).zfill(3)
    b.append(CaThi(ma,input()))

b.sort(key=lambda a:(a.nt,a.gt,a.grt))
for i in b:
    print(i)