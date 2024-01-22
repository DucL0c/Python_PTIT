from datetime import datetime
class PhiM:
    def __init__(self,maP,loaI,date,tenP,soTap):
        self.maP = maP
        self.loaI = loaI
        self.date = datetime.strptime(date,"%d/%m/%Y")
        self.tenP = tenP
        self.soTap = soTap
    def __str__(self):
        return f'{self.maP} {self.loaI} {self.date.strftime("%d/%m/%Y")} {self.tenP} {self.soTap}'
    
n,m = map(int,input().split())
a = []
b = []
for i in range(n):
    b.append(input())
for i in range(m):
    maP = 'P' + str(i+1).zfill(3)
    loaI_phiM = input()
    tmp = int(loaI_phiM[2:])
    loaI = b[tmp-1]
    date = input()
    tenP = input()
    soTap = int(input())
    phim_a = PhiM(maP,loaI,date,tenP,soTap)
    a.append(phim_a)
a.sort(key=lambda phim_a:(phim_a.date,phim_a.tenP,-phim_a.soTap))
for i in a:
    print(i)