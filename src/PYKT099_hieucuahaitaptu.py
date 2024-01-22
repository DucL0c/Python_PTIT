a = []
b = []
with open("DATA1.in",'r') as file:
    line = file.readlines()
    for i in line:
        a += i.lower().split()
with open("DATA2.in",'r') as file:
    line = file.readlines()
    for i in line:
        b += i.lower().split()
a_b = list(set(a).difference(set(b)))
b_a = list(set(b).difference(set(a)))
for i in sorted(a_b):
    print(i,end = " ")
print()
for i in sorted(b_a):
    print(i,end = " ")