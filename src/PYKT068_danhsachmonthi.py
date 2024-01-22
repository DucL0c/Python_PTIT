class MonHoc:
    def __init__(self, ma, ten, htt):
        self.ma = ma
        self.ten = ten
        self.htt = htt

    def __str__(self):
        return f"{self.ma} {self.ten} {self.htt}"


n = int(input())
a = []
for _ in range(n):
    a.append(MonHoc(input(), input(), input()))
a.sort(key=lambda a: (a.ma))
for i in a:
    print(i)
