class number:
    def __init__(self,n):
        self.val = n
        self.sum = 0
        while n>0:
            self.sum = self.sum + int(n%10)
            n /= 10

def cmp(a):
    return (a.sum,a.val)

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    l = []
    for i in a:
        l.append(number(i))
    l.sort(key = cmp)
    for i in l:
        print(i.val,end=" ")
    print()