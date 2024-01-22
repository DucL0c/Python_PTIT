class Oto:
    def __init__(self,s):
        self.bsx = s[0]
        self.lx = s[1]
        self.sg = int(s[2])
        self.dc = s[3]
        self.ng = s[4]
        self.dg = 0
        if self.dc == "OUT": self.dg = 0
        else:
            if self.lx == "Xe_con":
                if self.sg == 5: 
                    self.dg = 10000
                else: 
                    self.dg = 15000
            elif self.lx == "Xe_tai":
                if self.sg ==2: 
                    self.dg = 20000
            else:
                if self.sg == 29: 
                    self.dg = 50000
                else: 
                    self.dg = 70000
    
    def __str__(self):
        return self.ng
                  

n = int(input())
l = []
for i in range(n):
    s = input().split()
    l.append(Oto(s))
m = {}
for i in l:
    if i.ng not in m:
        m[i.ng] = i.dg
    else:
        m[i.ng] += i.dg
for i,j in m.items():
    print(f"{i}: {j}")