n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

giao = list(set(a).intersection(set(b)))
giao.sort()
for i in giao:
    print(i,end=" ")
print()

a_b = list(set(a).difference((set(b))))
a_b.sort()
for i in a_b:
    print(i,end=" ")
print()

b_a = list(set(b).difference((set(a))))
b_a.sort()
for i in b_a:
    print(i,end=" ")