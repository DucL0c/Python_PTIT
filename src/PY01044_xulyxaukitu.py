s1 = input().lower().split()
s2 = input().lower().split()
hop = list(set(s1).union(set(s2)))
giao = list(set(s1).intersection(set(s2)))
hop.sort()
giao.sort()
for i in hop:
    print(i,end=" ")
print()
for i in giao:
    print(i,end=" ")
print()