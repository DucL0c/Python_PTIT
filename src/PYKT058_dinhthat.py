def dfs(n,i,u,v,a):
    q,check = [u],[0]*(n+1)
    while len(q)>0:
        x = q.pop()
        if x==v: return False
        for j in a[x]:
            if j!=i and check[j]==0:
                q.append(j)
                check[j] = 1
    return True
  
t = int(input())
for i in range(t):
    n,m,u,v = map(int,input().split())
    a = []
    for _ in range(n+1):
        a.append([])
    for _ in range(m):
        x,y = map(int,input().split())
        a[x].append(y)

    ans = 0
    for i in range(1,n+1):
        if i!=u and i!= v and dfs(n,i,u,v,a):
            ans+=1
    print(ans)