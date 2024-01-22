class SinhVien:
    def __init__(self,maSV,tenSV,lopSV):
        self.maSV = maSV
        self.tenSV = tenSV
        self.lopSV = lopSV
    def add(self,diem):
        self.diem = diem
    def __str__(self):
        if self.diem == 0:
            return f'{self.maSV} {self.tenSV} {self.lopSV} {self.diem} KDDK'
        else:
            return f'{self.maSV} {self.tenSV} {self.lopSV} {self.diem}'
    
n = int(input())
a = []
for i in range(n):
    maSV = input()
    tenSV = input()
    lopSV = input()
    sv_a = SinhVien(maSV,tenSV,lopSV)
    a.append(sv_a)

for i in range(n):
    ma,s = input().split()
    diem = 10
    for j in s:
        if j == 'x':
            continue
        elif j == 'm':
            diem -= 1
        elif j == 'v':
            diem -= 2
    if diem<0: diem = 0
    for j in a:
        if j.maSV == ma:
            j.add(diem)
for i in a:
    print(i)