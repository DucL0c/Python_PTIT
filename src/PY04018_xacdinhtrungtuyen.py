class GiaoVien:
    def __init__(self,maGV,tenGV,mon,diem,loai):
        self.maGV = maGV
        self.tenGV = tenGV
        self.mon = mon
        self.diem = diem
        self.loai = loai
    def __str__(self):
        self.diem = '{:.1f}'.format(self.diem)
        return f'{self.maGV} {self.tenGV} {self.mon} {self.diem} {self.loai}'

n = int(input())
a = []
for i in range(n):
    maGV = "GV" + str(i+1).zfill(2)
    tenGV = input()
    maXT = input()
    d1 = float(input())
    d2 = float(input())
    monH = ''
    if maXT[0] == 'A': monH = 'TOAN'
    elif maXT[0] == 'B': monH = 'LY'
    elif maXT[0] == 'C': monH = 'HOA'

    tong = 0
    if maXT[1] == '1': tong = d1*2 + d2 + 2.0
    elif maXT[1] == '2': tong = d1*2 + d2 + 1.5
    elif maXT[1] == '3': tong = d1*2 + d2 + 1.0
    elif maXT[1] == '4': tong = d1*2 + d2 + 0.0
    
    loai = ''
    if tong>=18: loai = "TRUNG TUYEN" 
    else: loai = "LOAI "
    gv_a = GiaoVien(maGV,tenGV,monH,tong,loai) 
    a.append(gv_a)

a.sort(key = lambda gv_a:(-gv_a.diem))
for i in a:
    print(i)