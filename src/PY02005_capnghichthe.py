n = int(input())
a = list(map(int,input().split()))
dem = 0
for i in range(n-1):
    for j in range(i+1,n):
        if a[j]<a[i]:
            dem+=1
print(dem)