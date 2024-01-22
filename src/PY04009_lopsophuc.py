class SoPhuc:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def tong(self,a,b):
        self.x = a.x+b.x
        self.y = a.y+b.y
        return self
    
    def tich(self,a,b):
        self.x = a.x*b.x - a.y*b.y
        self.y = a.x*b.y + a.y*b.x
        return self

    def __str__(self):
        if self.y>0:
            return f'{self.x} + {self.y}i'
        else:
            return f'{self.x} - {abs(self.y)}i'
    
n = int(input())
for i in range(n):
    s = list(map(int,input().split()))
    a = SoPhuc(s[0],s[1])
    b = SoPhuc(s[2],s[3])

    t = SoPhuc(None,None)
    c = SoPhuc(None,None)
    d = SoPhuc(None,None)
    t = t.tong(a,b)
    c = c.tich(t,a)
    d = d.tich(t,t)

    print(f'{c}, {d}')