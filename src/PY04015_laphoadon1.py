class KH:
    def __init__(self,ma,ten,tien):
        self.ma = ma
        self.ten = ten
        self.tien = tien

    def __str__(self):
        return f'{self.ma} {self.ten} {self.tien}'
    
n = int(input())
l = []
for i in range(n):
    ma = "KH" + str(i+1).zfill(2)
    ten = input()
    st = int(input())
    end = int(input())
    tien = 0
    ds = end - st
    if ds<=50:
        tien = ds*100 + ds*100*0.02
    elif ds>50 and ds<=100:
        tien = (50*100 + (ds-50)*150) + (50*100 + (ds-50)*150)*0.03
    else:
        tien = (50*100 + 50*150 +(ds-100)*200) + (50*100 + 50*150 +(ds-100)*200)*0.05
    l.append(KH(ma,ten,round(tien)))

l.sort(key=lambda a:(-a.tien))
for i in l:
    print(i)