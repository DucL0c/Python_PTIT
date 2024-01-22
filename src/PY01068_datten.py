n,k = map(int,input().split())
a = input().split()
l = sorted(set(a))
def Try(a, k, start=0, ans=[]):
    if len(ans) == k:
        for i in ans:
            print(i,end=" ")
        print()
        return

    for i in range(start, len(a)):
        ans.append(a[i])
        Try(a, k, i + 1, ans)
        ans.pop()
Try(l,k,0,[])