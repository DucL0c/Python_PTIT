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

n,k = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
myMap = {}
l = []
for i in arr:
    if i not in myMap:
        l.append(i)
        myMap[i]=1
Try(l,k)