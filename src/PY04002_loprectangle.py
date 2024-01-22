def convert(s:str):
    return s.lower().title()

class Rectangle:
    def __init__(self,a,b,color):
        self.a = a
        self.b = b
        self.c = color
    def perimeter(self):
        return (self.a+self.b)*2
    def area(self):
        return self.a*self.b
    def color(self):
        return convert(self.c)

arr = input().split()
if int(arr[0]) > 0 and int(arr[1]) > 0:
    r = Rectangle(int(arr[0]), int(arr[1]), str(arr[2]))
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
else:
    print('INVALID')