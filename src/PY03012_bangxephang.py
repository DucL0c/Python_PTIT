class SinhVien:
    def __init__(self,ten,so_bai,sub):
        self.ten = ten
        self.so_bai = so_bai
        self.sub = sub
    def __str__(self):
        return f"{self.ten} {self.so_bai} {self.sub}"
    
def cmp(sv):
    return -sv.so_bai, sv.sub, sv.ten

n = int(input())
l = []
for _ in range(n):
    t = input()
    a,b = map(int,input().split())
    sv = SinhVien(t,a,b)
    l.append(sv)
tmp = sorted(l, key = cmp)
for i in tmp:
    print(i)