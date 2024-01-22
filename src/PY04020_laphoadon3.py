class HD:
    def __init__(self, ma, ten, sl, gia, ck):
        self.ma = ma
        self.ten = ten
        self.sl = sl
        self.gia = gia
        self.ck = ck
        self.tong = self.sum()

    def sum(self):
        return self.sl*self.gia-self.ck

    def __str__(self):
        return f'{self.ma} {self.ten} {self.sl} {self.gia} {self.ck} {self.tong}'


n = int(input())
l = []
for _ in range(n):
    l.append(HD(input(), input(), int(input()), int(input()), int(input())))
l.sort(key=lambda a:(-a.tong))
for i in l:
    print(i)