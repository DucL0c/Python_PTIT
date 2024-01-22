class HocSinh:
    def __init__(self,maHs,tenHs,diemTb,xepLoai):
        self.maHS = maHs
        self.tenHS = tenHs
        self.diemTb = diemTb
        self.xepLoai = xepLoai
    def __str__(self):
        self.diemTb = '{:.1f}'.format(self.diemTb)
        return f'{self.maHS} {self.tenHS} {self.diemTb} {self.xepLoai}'

n = int(input())
l = []
for i in range(n):
    maHS = 'HS' + str(i+1).zfill(2)
    tenHS = input()
    a = list(map(float,input().split()))
    tong = a[0]*2 + a[1]*2
    for j in range(2,10):
        tong += a[j]
    diemTb = tong/10/1.2
    xepLoai = ''
    if diemTb>=9: xepLoai = 'XUAT SAC'
    elif diemTb>=8 and diemTb<=8.9 : xepLoai = 'GIOI'
    elif diemTb>=7 and diemTb<=7.9 : xepLoai = 'KHA'
    elif diemTb>=5 and diemTb<=6.9 : xepLoai = 'TB'
    elif diemTb<5 : xepLoai = 'YEU'
    hs_a =  HocSinh(maHS,tenHS,diemTb,xepLoai)
    l.append(hs_a)
l.sort(key=lambda hs_a:(-hs_a.diemTb,hs_a.maHS))
for i in l:
    print(i)