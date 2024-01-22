from datetime import datetime
class CaThi:
    def __init__(self,ma,ngay,gio,phong):
        self.ma = ma
        self.ngay = ngay
        self.gio = gio
        self.phong = phong
    
    def __str__(self):
        return f"{self.ma} {self.ngay} {self.gio} {self.phong}"

a = [] 
with open('CATHI.in','r') as file:
    n = int(file.readline().strip())
    for i in range(n):
        ma = "C" + str(i+1).zfill(3)
        a.append(CaThi(ma,file.readline().strip(),
                       file.readline().strip(),file.readline().strip()))
a.sort(key=lambda a:(a.ngay,a.gio,a.ma))
for i in a:
    print(i)