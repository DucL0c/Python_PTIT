class GD:
    def __init__(self, i, ten, dm, sd):
        self.ma = self.setID(i)
        self.ten = self.setN(ten)
        self.tdm = self.TDM(dm, sd)
        self.vdm = self.VDM(dm, sd)
        self.vat = self.VAT()
        self.tong = self.tdm+self.vdm+self.vat

    def setID(self, i):
        return "KH" + str(i+1).zfill(2)

    def setN(self, ten: str):
        s = ten.lower().split()
        a = []
        for i in s:
            a.append(i.title())
        return ' '.join(a)

    def TDM(self, dm, sd):
        if dm == 'A':
            if sd < 100:
                return sd*450
            else:
                return 100*450
        elif dm == 'B':
            if sd < 500:
                return sd*450
            else:
                return 500*450
        elif dm == 'C':
            if sd < 200:
                return sd*450
            else:
                return 200*450

    def VDM(self, dm, sd):
        if dm == 'A' and sd >= 100:
            return (sd-100)*1000
        elif dm == 'B' and sd >= 500:
            return (sd-500)*1000
        elif dm == 'C' and sd >= 200:
            return (sd-200)*1000
        return 0

    def VAT(self):
        return 0.05*self.vdm

    def __str__(self):
        return f'{self.ma} {self.ten} {round(self.tdm)} {round(self.vdm)} {round(self.vat)} {round(self.tong)}'


n = int(input())
l = []
for i in range(n):
    ten = input()
    s = input().split()
    dm = s[0]
    sd = int(s[2]) - int(s[1])
    l.append(GD(i, ten, dm, sd))
l.sort(key=lambda a:(-a.tong))
for i in l:
    print(i)