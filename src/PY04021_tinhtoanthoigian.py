from datetime import datetime

class GT:
    def __init__(self,ma,ten,tg,ds):
        self.ma = ma
        self.ten = ten
        self.tg = tg
        self.ds = ds
    def __str__(self):
        return f"{self.ma} {self.ten} {self.tg}"
    
n = int(input())
l = []
for i in range(n):
    ma = input()
    ten = input()
    st = input()
    end = input()

    tmp = datetime.strptime(end,"%H:%M") - datetime.strptime(st,"%H:%M")
    ds = h = tmp.total_seconds() / 3600
    h = tmp.total_seconds() // 3600
    p = (tmp.total_seconds()//60) %60 
    tg = f"{int(h)} gio  {int(p)} phut"

    l.append(GT(ma=ma,ten=ten,tg=tg,ds=ds))

l.sort(key=lambda a:(-a.ds))
for i in l:
    print(i)