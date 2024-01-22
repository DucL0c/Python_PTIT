t = int(input())
fi = {}
def FI():
    fi[1] = 1
    fi[2] = 1
    for i in range(3,93,1):
        fi[i] = fi[i-1] + fi[i-2]

for _ in range(t):
    a,b = list(map(int,input().split()))
    FI()
    for i in range(a,b+1,1):
        print(fi[i],end = " ")
    print()
