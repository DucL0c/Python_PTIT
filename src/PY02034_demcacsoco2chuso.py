import re

r = '\d\d'
s = input()
myMap = {}
l = re.findall(r,s)
for i in l:
    if i not in myMap:
        myMap[i] = 1
    else:
        myMap[i] += 1
for i,j in myMap.items():
    print(f"{i} {j}")