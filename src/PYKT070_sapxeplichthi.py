class MonThi:
    def __init__(self,maM,tenM,htt):
        self.maM = maM
        self.tenM = tenM
        self.htt = htt

class CaThi:
    def __init__(self,maC,nt,gt,pt):
        self.maC = maC
        self.nt = nt
        self.gt = gt
        self.pt = pt

class LichThi:
    def __init__(self,tmp:str):
        tmp = tmp.split()
        self.maC = tmp[0]
        self.maM = tmp[1]

        self.nt = None
        self.gt = None
        self.pt = None
        self.tenM = None
        self.mt = None
        self.mn = tmp[2]
        self.ssv = tmp[3] 
        for i in b:
            if i.maC == self.maC:
                self.nt = i.nt
                self.gt = i.gt
                self.pt = i.pt
                break
        for i in a:
            if i.maM == self.maM:
                self.tenM = i.tenM
                break
    def __str__(self):
        return f'{self.nt} {self.gt} {self.pt} {self.tenM} {self.mn} {self.ssv}'

a = []
with open("MONTHI.in","r") as file:
    n = file.readline()
    for i in range(int(n)):
        a.append(MonThi(file.readline().strip(),file.readline().strip(),file.readline().strip()))
    file.close()

b = []
with open("CATHI.in","r") as file:
    n = file.readline()
    for i in range(int(n)):
        ma = 'C' + str(i+1).zfill(3)
        b.append(CaThi(ma,file.readline().strip(),file.readline().strip(),file.readline().strip()))
    file.close()

c = []
with open("LICHTHI.in","r") as file:
    n = file.readline()
    for i in range(int(n)):
        c.append(LichThi(file.readline().strip()))
    file.close()

c.sort(key=lambda a:(a.nt,a.gt,a.maC))
for i in c:
    print(i)