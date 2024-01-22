def init():
    for i in range(1,n+1):
        parent[i] = i
        num[i] = 1
def find(u:int):
    if u!=parent[u]:
        parent[u] = find(parent[u])
    return parent[u]
def union(u:int, v:int):
    a = find(u)
    b = find(v)
    # if a==b: return True
    if num[a]<num[b]:
        a,b = b,a
    parent[b] = a
    num[a] += num[b]

n,m,k = map(int,input().split())
parent = [0]*(n+1)
num = [0]*(n+1)
init()
for i in range(m):
    x,y = map(int,input().split())
    union(x,y)
d = 0
for i in range(1,n+1):
    if parent[i] != parent[k]:
        print(i)
        d = 1
if d==0:
    print(0)