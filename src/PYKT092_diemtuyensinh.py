class ThiSinh:
    def __init__(self,maTS,tenTS,diem,tt):
        self.maTS = maTS
        self.tenTS = tenTS
        self.diem = diem
        self.tt = tt
    def __str__(self):
        self.diem = '{:.1f}'.format(self.diem)
        return f'{self.maTS} {self.tenTS} {self.diem} {self.tt}'
    
n = int(input())
l = []
for i in range(n):
    maTS = 'TS' + str(i+1).zfill(2)
    ten = input().strip().lower().split()
    tenTS = ""
    for j in ten:
        tenTS += j.title()+" "
    diem = float(input())
    dt = input()
    kv = int(input())

    if kv==1: diem += 1.5
    elif kv==2: diem += 1

    if dt != 'Kinh': diem += 1.5

    tt = ''
    if diem>=20.5: tt = 'Do'
    else: tt = 'Truot'

    a = ThiSinh(maTS,tenTS,diem,tt)
    l.append(a)

l.sort(key=lambda a:(-a.diem,a.maTS))
for i in l:
    print(i)