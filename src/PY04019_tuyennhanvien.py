class NhanVien:
    def __init__(self,maNV,tenNV,diemTB,xL):
        self.maNV = maNV
        self.tenNV = tenNV
        self.diemTB = diemTB
        self.xL = xL
    def __str__(self):
        self.diemTB = '{:.2f}'.format(self.diemTB)
        return f"{self.maNV} {self.tenNV} {self.diemTB} {self.xL}"
    
n = int(input())
l = []
for i in range(n):
    maNV = 'TS0' + str(i+1)
    tenNV = input()
    d1 = float(input())
    d2 = float(input())
    if d1>10: d1 /= 10
    if d2>10: d2 /= 10

    diemTb = (d1+d2)/2
    xepLoai = ""
    if diemTb>9.5: xepLoai = 'XUAT SAC'
    elif diemTb>=8 and diemTb<=9.5 : xepLoai = 'DAT'
    elif diemTb>=5 and diemTb<8 : xepLoai = 'CAN NHAC'
    elif diemTb<5 : xepLoai = 'TRUOT'

    nv_a = NhanVien(maNV,tenNV,diemTb,xepLoai)
    l.append(nv_a)

l.sort(key=lambda nv_a:(-nv_a.diemTB))
for i in l:
    print(i)