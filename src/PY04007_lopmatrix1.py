class Matrix:
    def __init__(self,n,m):
        self.n = n
        self.m = m
        self.a = []
        self.b = []
    def ip(self):
        for i in range(self.n):
            l = list(map(int,input().split()))
            (self.a).append(l)

    def transpose(self):
        for j in range(self.m):
            l = []
            for i in range(self.n):
                l.append(self.a[i][j])
            self.b.append(l)

    def out(self):
        for i in range(self.n):
            for j in range(self.n):
                s = 0
                for k in range(self.m):
                    s += self.a[i][k]*self.b[k][j] 
                print(s,end=" ")
            print()

for _ in range(int(input())):
    n,m = map(int,input().split())
    a = Matrix(n,m)
    a.ip()
    a.transpose()
    a.out()





# for _ in range(int(input())):
#     n,m = map(int,input().split())
#     a = []
#     a_t = []
#     for i in range(n):
#         a.append(list(map(int,input().split())))
#     for j in range(m):
#         row = []
#         for i in range(n):
#             row.append(a[i][j])
#         a_t.append(row)
#     for i in range(n):
#         for j in range(n):
#             s = 0
#             for k in range(m):
#                 s += a[i][k]*a_t[k][j]
#             print(s,end=" ")
#         print()