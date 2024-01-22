class number:
    def __init__(self,n):
        self.val = n
        self.tich = 1
        while n>0:
            self.tich *= n%10
            n //= 10
def cmp(a):
    return (a.tich,a.val)
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    l = []
    for i in a:
        l.append(number(i))
    l.sort(key=cmp)
    for i in l:
        print(i.val,end=" ")
    print()