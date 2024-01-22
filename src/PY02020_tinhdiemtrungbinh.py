n = int(input())
a = list(map(float,input().split()))
sum = 0
dem = 0
for i in a:
    if i != min(a) and i!=max(a):
        sum += i
        dem += 1
avr = sum/dem
print("%.2f" %(avr))