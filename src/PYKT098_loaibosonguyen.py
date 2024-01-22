def check(s:str):
    tong = 0
    for i in range(len(s)):
        if s[i].isalpha():
            return True
        else:
            tong = tong*10 + int(s[i])
    if tong>int(1e9) or tong<-int(1e9):
        return True
    return False

a = []
with open("DATA.in",'r') as file: 
    line = file.readlines()
    for i in line:
        for j in i.strip().split():
            if check(j)==True:
                a.append(j)

a.sort()
for i in a:
    print(i,end=' ')