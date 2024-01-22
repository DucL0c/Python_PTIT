class NV:
    def __init__(self, ma, ten, lg, sn):
        self.ma = ma
        self.ten = ten
        self.phg = self.room()
        self.lg = self.salary(lg,sn)

    def room(self):
        for i in a:
            if i[0] == self.ma[-2:]:
                return ' '.join(i[1:])

    def salary(self, lg, sn):
        if self.ma[0] == 'A':
            if int(self.ma[1:3]) >= 1 and int(self.ma[1:3]) <= 3:
                return lg*sn*10*1000
            elif int(self.ma[1:3]) >= 4 and int(self.ma[1:3]) <= 8:
                return lg*sn*12*1000
            elif int(self.ma[1:3]) >= 9 and int(self.ma[1:3]) <= 15:
                return lg*sn*14*1000
            elif int(self.ma[1:3]) >= 16:
                return lg*sn*20*1000
        elif self.ma[0] == 'B':
            if int(self.ma[1:3]) >= 1 and int(self.ma[1:3]) <= 3:
                return lg*sn*10*1000
            elif int(self.ma[1:3]) >= 4 and int(self.ma[1:3]) <= 8:
                return lg*sn*11*1000
            elif int(self.ma[1:3]) >= 9 and int(self.ma[1:3]) <= 15:
                return lg*sn*13*1000
            elif int(self.ma[1:3]) >= 16:
                return lg*sn*16*1000
        elif self.ma[0] == 'C':
            if int(self.ma[1:3]) >= 1 and int(self.ma[1:3]) <= 3:
                return lg*sn*9*1000
            elif int(self.ma[1:3]) >= 4 and int(self.ma[1:3]) <= 8:
                return lg*sn*10*1000
            elif int(self.ma[1:3]) >= 9 and int(self.ma[1:3]) <= 15:
                return lg*sn*12*1000
            elif int(self.ma[1:3]) >= 16:
                return lg*sn*14*1000
        elif self.ma[0] == 'D':
            if int(self.ma[1:3]) >= 1 and int(self.ma[1:3]) <= 3:
                return lg*sn*8*1000
            elif int(self.ma[1:3]) >= 4 and int(self.ma[1:3]) <= 8:
                return lg*sn*9*1000
            elif int(self.ma[1:3]) >= 9 and int(self.ma[1:3]) <= 15:
                return lg*sn*11*1000
            elif int(self.ma[1:3]) >= 16:
                return lg*sn*13*1000
    
    def __str__(self):
        return f'{self.ma} {self.ten} {self.phg} {self.lg}'

n = int(input())
a = []
for _ in range(n):
    a.append(input().split())

m = int(input())
l = []
for _ in range(m):
    ma = input()
    ten = input()
    lg = int(input())
    sn = int(input())
    l.append(NV(ma,ten,lg,sn))

for i in l:
    print(i)