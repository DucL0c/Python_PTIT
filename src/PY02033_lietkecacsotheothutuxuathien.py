import re
r = '\d\d'
s = input()
a = re.findall(r, s)
myMap = {}
for i in a:
    if i not in myMap:
        myMap[i] = 1
        print(i,end=" ")