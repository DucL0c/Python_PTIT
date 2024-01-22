class ThiSinh:
    def __init__(self,ten,ns,tong):
        self.ten = ten
        self.ns = ns
        self.tong = tong
    def __str__(self):
        self.tong = '{:.1f}'.format(self.tong)
        return f"{self.ten} {self.ns} {self.tong}"
    
ten = input()
ns = input()
d1 = float(input())
d2 = float(input())
d3 = float(input())
a = ThiSinh(ten,ns,d1+d2+d3)
print(a)