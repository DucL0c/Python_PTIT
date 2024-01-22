class Team:
    def __init__(self,ma,tenTeam,tenTruong):
        self.ma = ma
        self.tenTeam = tenTeam
        self.tenTruong = tenTruong
    def __str__(self):
        return f'{self.ma} {self.tenTeam} {self.tenTruong}'

class ThiSinh:
    def __init__(self,maTS,ht,maTeam):
        self.maTS = maTS
        self.ht = ht
        self.tenTeam = None
        self.tenTruong = None
        for i in a:
            if i.ma == maTeam:
                self.tenTeam = i.tenTeam
                self.tenTruong = i.tenTruong
                break
    def __str__(self):
        return f"{self.maTS} {self.ht} {self.tenTeam} {self.tenTruong}"


t = int(input())
a = []
for i in range(t):
    ma = 'Team' + str(i+1).zfill(2)
    a.append(Team(ma,input(),input()))

n = int(input())
b = []
for i in range(n):
    ma = 'C' + str(i+1).zfill(3)
    b.append(ThiSinh(ma,input(),input()))
b.sort(key=lambda a:(a.ht))
for i in b:
    print(i)