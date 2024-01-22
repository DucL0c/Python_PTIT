class Matrix:
    def __init__(self,n,m,a):
        self.n = n
        self.m = m
        self.a = a
    def tic(self,b):
        for i in range(self.n):
            for j in range(self.n):
                s = 0
                for k in range(self.m):
                    s += self.a[i][k]*b[k][j] 
                print(s,end=" ")
            print()
k = 0
l = []
for _ in range(int(input())):
    l += list(map(int,input().split()))
    a, a_t= [],[]
    for i in range(l[k]):
        a.append(list(map(int,input().split())))   
    matrix = Matrix(l[k],l[k+1],a)
    for j in range(l[k+1]):
        row = []
        for i in range(l[k]):
            row.append(a[i][j])
        a_t.append(row)
    matrix.tic(a_t)
    k += 2