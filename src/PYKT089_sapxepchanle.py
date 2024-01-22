n = int(input())
count = 0
a = []
while count<n:
    line = input()
    line = line.split()
    for i in line:
        count += 1
        a.append(int(i))
chan = []
le = []
for i in a:
    if i%2==0:
        chan.append(i)
    else:
        le.append(i)
chan.sort()
le.sort(reverse=True)
for i in range(n):
    if a[i]%2==0:
        print(chan.pop(0),end=" ")
    else:
        print(le.pop(0),end=" ")