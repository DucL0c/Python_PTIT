from datetime import datetime
class DLM:
    def __init__(self,ma,tenTram,tg,lm):
        self.ma = ma
        self.tenTram = tenTram
        self.tg = tg
        self.lm = lm

    def __str__(self):
        x = '{:.2f}'.format(self.lm/self.tg)
        return f'{self.ma} {self.tenTram} {x}'

n = int(input())
l = []
for i in range(n):
    ma = "T" + str(i+1).zfill(2)
    ten = input()
    st = input()
    end = input()
    lm = int(input())

    tmp = datetime.strptime(end,"%H:%M") - datetime.strptime(st,"%H:%M")
    ds = tmp.total_seconds() / 3600
    if len(l) == 0:
        l.append(DLM(ma,ten,ds,lm))
    else:
        d = 0
        for i in l:
            if i.tenTram == ten:
                i.tg += ds
                i.lm += lm
                d = 1
        if d==0:
            l.append(DLM(ma,ten,ds,lm))
        
for i in l:
    print(i)