import math
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def distance(self,b):
        return math.sqrt((self.x-b.x)**2+(self.y-b.y)**2)
    
i = 0
l = []
for _ in range(int(input())):
    l += list(map(float,input().split()))
    a = Point(l[i],l[i+1])
    b = Point(l[i+2],l[i+3])
    c = Point(l[i+4],l[i+5])
    A = a.distance(b)
    B = b.distance(c)
    C = c.distance(a)
    if A+B>C and B+C>A and C+A>B:
        p = (A+B+C)/2
        print('{:.2f}'.format(math.sqrt(p*(p-A)*(p-B)*(p-C))))
    else:
        print("INVALID")
    i+=6



# import math
# class Point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#     def distance(self,b):
#         return math.sqrt((self.x-b.x)**2+(self.y-b.y)**2)
    
# class Triangle:
#     def __init__(self,p1:Point,p2:Point,p3:Point):
#         self.p1 = p1
#         self.p2 = p2
#         self.p3 = p3
#     def solve(self):
#         a = self.p1.distance(self.p2)
#         b = self.p2.distance(self.p3)
#         c = self.p3.distance(self.p1)
#         if max(a, b, c) * 2 >= a + b + c:
#             print("INVALID")
#         else:
#             print(f"{a + b + c:.3f}")

# i = 0
# l = []
# for _ in range(int(input())):
#     l += list(map(float,input().split()))
#     a = Point(l[i],l[i+1])
#     b = Point(l[i+2],l[i+3])
#     c = Point(l[i+4],l[i+5])
#     tri = Triangle(a,b,c)
#     tri.solve()
#     i+=6