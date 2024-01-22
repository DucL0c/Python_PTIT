n = int(input())
a = list(map(int,input().split()))
a.sort()
max1 = a[0]*a[1]
max2 = a[n-1]*a[n-2]
max3 = a[0]*a[n-1]
max4 = a[0]*a[1]*a[2]
max5 = a[n-1]*a[n-2]*a[n-3]
max6 = a[0]*a[1]*a[n-1]
max7 = a[0]*a[n-1]*a[n-2]
print(max(max1,max2,max3,max4,max5,max6,max7))